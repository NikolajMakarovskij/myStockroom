import { React, useState, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import CustomTextField from '../../Forms/TextField.jsx'
import { useForm } from 'react-hook-form'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import AxiosInstanse from '../../Axios.jsx'
import { useNavigate, Link } from 'react-router-dom'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import useCSRF from '../../Hooks/CSRF.jsx'
import PrintError from '../../Errors/Error.jsx'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function CreateConsumableCategory() {
  const CSRF = useCSRF()
  const [errorEdit, setErrorEdit] = useState(null)
  const navigate = useNavigate()
  const defaultValues = {
    name: '',
    slug: '',
  }

  const schema = yup
    .object({
      name: yup.string().required('Обязательное поле').max(50, 'Должно быть короче 50 символов'),
      slug: yup
        .string()
        .required('Обязательное поле')
        .min(3, 'Must have at least 3 characters.')
        .max(16, 'Cannot be longer than 16 characteres.')
        .lowercase()
        .trim()
        .matches(
          /^(?![0-9-]+$)(?:[a-z]{2,}-?|[0-9]-?)+(?<!-)$/gm,
          'Должно начинаться с буквы и может содержать только буквы, цифры или тире (не более одного подряд).',
        ),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `consumables/consumable_category/`,
      {
        name: data.name,
        slug: data.slug,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/consumables/categories/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })
  return (
    <>
      <form onSubmit={handleSubmit(submission)}>
        <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
          <Typography>Добавить группу</Typography>
        </Box>
        <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
          <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
            <CustomTextField
              label='Группа'
              placeholder='Введите название группы'
              name='name'
              control={control}
              width={'30%'}
              maxlength='50'
            />
            <CustomTextField
              label='Ссылка'
              placeholder='Введите ссылку'
              name='slug'
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
                <Button variant='contained' component={Link} to={`/consumables/categories/list`}>
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
