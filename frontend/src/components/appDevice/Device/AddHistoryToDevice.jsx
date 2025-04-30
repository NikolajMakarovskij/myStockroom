import { React, useState, useEffect, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import { useForm } from 'react-hook-form'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import AxiosInstanse from '../../Axios.jsx'
import { useNavigate, useParams, Link } from 'react-router-dom'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import PrintError from '../../Errors/Error.jsx'
import useCSRF from '../../Hooks/CSRF.jsx'
import LinearIndeterminate from '../../appHome/ProgressBar.jsx'
import MultilineField from '../../Forms/MultilineField.jsx'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

const AddHistoryToDevice = () => {
  const CSRF = useCSRF()
  const deviceParam = useParams()
  const deviceId = deviceParam.id
  const [user, setUser] = useState(null)
  const [errorEdit, setErrorEdit] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  const GetUser = useCallback(async () => {
    try {
      await AxiosInstanse.get(`whoami/`).then((res) => {
        setUser(res.data)
      })
    } catch (error) {
      setError(error.message)
    } finally {
      setLoading(false)
    }
  })

  useEffect(() => {
    Promise.all([GetUser()])
  }, [])

  const defaultValues = {
    model_id: '',
    status_choice: '',
    note: '',
    username: '',
  }

  const schema = yup
    .object({
      status_choice: yup.string().required('Обязательное поле'),
      note: yup.string().max(1000, 'Должно быть короче 1000 символов').required('Обязательное поле'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `stockroom/add_device_history/`,
      {
        model_id: deviceId,
        status_choice: data.status_choice,
        note: data.note,
        username: user.username,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/device/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })
  return (
    <form onSubmit={handleSubmit(submission)}>
      <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
        <Typography>Добавить на склад</Typography>
      </Box>
      {loading ? (
        <LinearIndeterminate />
      ) : error ? (
        <PrintError error={error} />
      ) : (
        <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
          <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
            <MultilineField
              label='Описание'
              placeholder='Опишите проблему'
              name='status_choice'
              control={control}
              width={'30%'}
              rows={4}
              maxlength='1000'
            />
            <MultilineField
              label='Примечание'
              placeholder='Введите примечание'
              name='note'
              control={control}
              width={'30%'}
              rows={4}
              maxlength='1000'
            />
          </Box>
          {!errorEdit ? (
            <></>
          ) : (
            <Box sx={{ display: 'flex', justifyContent: 'space-around', marginBottom: '40px' }}>
              <PrintError error={errorEdit} />
            </Box>
          )}
          <Box>
            <ThemeProvider theme={darkTheme}>
              <Box display='flex' justifyContent='space-between' alignItems='center'>
                <Button variant='contained' type='submit'>
                  Сохранить
                </Button>
                <Button variant='contained' component={Link} to={`/device/list`}>
                  Отмена
                </Button>
              </Box>
            </ThemeProvider>
          </Box>
        </Box>
      )}
    </form>
  )
}

export default AddHistoryToDevice
