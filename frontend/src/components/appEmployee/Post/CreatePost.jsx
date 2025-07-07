import { React, useState, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import CustomTextField from '../../Forms/TextField.jsx'
import { useForm } from 'react-hook-form'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import AxiosInstanse from '../../Axios.jsx'
import { useNavigate, Link } from 'react-router-dom'
import LinearIndeterminate from '../../appHome/ProgressBar.jsx'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import AutocompleteField from '../../Forms/AutocompleteField.jsx'
import useInterval from '../../Hooks/useInterval.jsx'
import useCSRF from '../../Hooks/CSRF.jsx'
import PrintError from '../../Errors/Error.jsx'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function CreatePost() {
  const CSRF = useCSRF()
  const [dep, setDeps] = useState()
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [errorEdit, setErrorEdit] = useState(null)
  const [delay, setDelay] = useState(100)
  const navigate = useNavigate()

  useInterval(() => {
    async function getData() {
      try {
        await AxiosInstanse.get(`employee/departament/`).then((res) => {
          setDeps(res.data)
          setLoading(false)
          setError(null)
          setDelay(5000)
        })
      } catch (error) {
        setError(error.message)
        setDelay(null)
      } finally {
        setLoading(false)
      }
    }
    getData()
  }, delay)

  const defaultValues = {
    name: '',
    departament: '',
  }

  const schema = yup
    .object({
      name: yup.string().required('Обязательное поле').max(50, 'Должно быть короче 50 символов'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `employee/post/`,
      {
        name: data.name,
        departament: data.departament,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/post/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })
  return (
    <div>
      {loading ? (
        <LinearIndeterminate />
      ) : (
        <form onSubmit={handleSubmit(submission)}>
          <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
            <Typography>Добавить должность</Typography>
          </Box>
          <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
            <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
              <CustomTextField
                label='Должность'
                placeholder='Введите должность'
                name='name'
                control={control}
                width={'30%'}
                maxlength='50'
              />
              <AutocompleteField
                loading={loading}
                error={error}
                name='departament'
                control={control}
                width={'30%'}
                options={dep}
                label='Выберите отдел'
                placeholder='Выберите отдел'
                noOptionsText='Отдел не обнаружен'
                optionLabel={(option) => `${option.name}`}
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
                  <Button variant='contained' component={Link} to={`/post/list`}>
                    Отмена
                  </Button>
                </Box>
              </ThemeProvider>
            </Box>
          </Box>
        </form>
      )}
    </div>
  )
}
