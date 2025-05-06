import { React, useState, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import CustomTextField from '../../Forms/TextField'
import { useForm } from 'react-hook-form'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import AxiosInstanse from '../../Axios'
import { useNavigate, Link } from 'react-router-dom'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import AutocompleteField from '../../Forms/AutocompleteField'
import useInterval from '../../Hooks/useInterval'
import useCSRF from '../../Hooks/CSRF.jsx'
import PrintError from '../../Errors/Error.jsx'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function CreateEmployee() {
  const CSRF = useCSRF()
  const [workplace, setWorkplaces] = useState()
  const [post, setPosts] = useState()
  const [loadingWP, setLoadingWP] = useState(true)
  const [loadingPost, setLoadingPost] = useState(true)
  const [errorWP, setErrorWP] = useState(null)
  const [errorPost, setErrorPost] = useState(null)
  const [errorEdit, setErrorEdit] = useState(null)
  const [delay, setDelay] = useState(100)
  const navigate = useNavigate()

  useInterval(() => {
    async function getPost() {
      try {
        await AxiosInstanse.get(`employee/post_list/`).then((res) => {
          setPosts(res.data)
          setErrorPost(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorPost(error.message)
        setDelay(null)
      } finally {
        setLoadingPost(false)
      }
    }
    async function getWp() {
      try {
        await AxiosInstanse.get(`workplace/workplace_list/`).then((res) => {
          setWorkplaces(res.data)
          setErrorWP(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorWP(error.message)
        setDelay(null)
      } finally {
        setLoadingWP(false)
      }
    }
    Promise.all([getPost(), getWp()])
  }, delay)

  const defaultValues = {
    name: '',
    last_name: '',
    surname: '',
    workplace: '',
    post: '',
    employeeEmail: '',
  }

  const schema = yup
    .object({
      name: yup.string().required('Обязательное поле').max(50, 'Должно быть короче 50 символов'),
      last_name: yup.string().max(50, 'Должно быть короче 50 символов'),
      surname: yup.string().max(50, 'Должно быть короче 50 символов'),
      employeeEmail: yup.string().email('Введите верный e-mail'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `employee/employee/`,
      {
        name: data.name,
        last_name: data.last_name,
        surname: data.surname,
        workplace: data.workplace,
        post: data.post,
        employeeEmail: data.employeeEmail,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/employee/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })
  return (
    <>
      <form onSubmit={handleSubmit(submission)}>
        <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
          <Typography>Добавить сотрудника</Typography>
        </Box>
        <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
          <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
            <CustomTextField
              label='Фамилия'
              placeholder='Введите фамилию'
              name='surname'
              control={control}
              width={'30%'}
              maxlength='50'
            />
            <CustomTextField
              label='Имя'
              placeholder='Введите имя'
              name='name'
              control={control}
              width={'30%'}
              maxlength='50'
            />
            <CustomTextField
              label='Отчество'
              placeholder='Введите отчество'
              name='last_name'
              control={control}
              width={'30%'}
              maxlength='50'
            />
          </Box>
          <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
            <AutocompleteField
              loading={loadingPost}
              error={errorPost}
              name='post'
              control={control}
              width={'30%'}
              options={post}
              label='Выберите должность'
              placeholder='Выберите должность'
              noOptionsText='Должность не обнаружена'
              optionLabel={(option) => `${option.name} (отдел: ${option.departament.name})`}
            />
            <AutocompleteField
              loading={loadingWP}
              error={errorWP}
              name='workplace'
              control={control}
              width={'30%'}
              options={workplace}
              label='Выберите рабочее место'
              placeholder='Выберите рабочее место'
              noOptionsText='Рабочее место не обнаружено'
              optionLabel={(option) => `${option.name} (кабинет: ${option.room.name} здание: ${option.room.building})`}
            />
            <CustomTextField
              label='E-mail'
              placeholder='Введите email'
              name='employeeEmail'
              control={control}
              width={'30%'}
              maxlength='50'
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
                <Button variant='contained' component={Link} to={`/employee/list`}>
                  Отмена
                </Button>
              </Box>
            </ThemeProvider>
          </Box>
        </Box>
      </form>
    </>
  )
}
