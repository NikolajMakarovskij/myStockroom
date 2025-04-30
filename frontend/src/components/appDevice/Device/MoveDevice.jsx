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
import AutocompleteField from '../../Forms/AutocompleteField.jsx'
import MultilineField from '../../Forms/MultilineField.jsx'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

const MoveDevice = () => {
  const CSRF = useCSRF()
  const deviceParam = useParams()
  const deviceId = deviceParam.id
  const [user, setUser] = useState(null)
  const [workplace, setWorkplace] = useState(null)
  const [errorEdit, setErrorEdit] = useState(null)
  const [loading, setLoading] = useState(true)
  const [loadingWorkplace, setLoadingWorkplace] = useState(true)
  const [error, setError] = useState(null)
  const [errorWorkplace, setErrorWorkplace] = useState(null)
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

  const GetWorkplace = useCallback(async () => {
    try {
      await AxiosInstanse.get(`workplace/workplace_list/`).then((res) => {
        setWorkplace(res.data)
      })
    } catch (error) {
      setErrorWorkplace(error.message)
    } finally {
      setLoadingWorkplace(false)
    }
  })

  useEffect(() => {
    Promise.all([GetUser(), GetWorkplace()])
  }, [])

  const defaultValues = {
    model_id: '',
    workplace_id: '',
    note: '',
    username: '',
  }

  const schema = yup
    .object({
      workplace_id: yup.string().required('Обязательное поле'),
      note: yup.string().max(1000, 'Должно быть короче 1000 символов').required('Обязательное поле'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `stockroom/move_device/`,
      {
        model_id: deviceId,
        workplace_id: data.workplace_id,
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
      {loading && loadingWorkplace ? (
        <LinearIndeterminate />
      ) : error ? (
        <PrintError error={error} />
      ) : (
        <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
          <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
            <AutocompleteField
              loading={loadingWorkplace}
              error={errorWorkplace}
              name='workplace_id'
              id='workplace_id'
              control={control}
              width={'30%'}
              options={workplace}
              label='Выберите рабочее место'
              placeholder='Выберите рабочее место'
              noOptionsText='Рабочее место не обнаружено'
              optionLabel={(option) => `${option.name} ${option.room.building} ${option.room.name}`}
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

export default MoveDevice
