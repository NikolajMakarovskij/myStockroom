import { React, useState, useEffect, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import CustomTextField from '../../Forms/TextField'
import { useForm } from 'react-hook-form'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import AxiosInstanse from '../../Axios'
import { useNavigate, useParams, Link } from 'react-router-dom'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import PrintError from '../../Errors/Error'
import useCSRF from '../../Hooks/CSRF'
import LinearIndeterminate from '../../appHome/ProgressBar'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function AddToStockConsumable() {
  const CSRF = useCSRF()
  const conParam = useParams()
  const conId = conParam.id
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
    GetUser()
  }, [])

  const defaultValues = {
    model_id: '',
    quantity: '',
    number_rack: '',
    number_shelf: '',
    username: '',
  }

  const schema = yup
    .object({
      quantity: yup.number('Введите целое число').integer('Введите целое число').required('Обязательное поле'),
      number_rack: yup.number('Введите целое число').integer('Введите целое число').required('Обязательное поле'),
      number_shelf: yup.number('Введите целое число').integer('Введите целое число').required('Обязательное поле'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `stockroom/add_to_stock_consumable/`,
      {
        model_id: conId,
        quantity: data.quantity,
        number_rack: data.number_rack,
        number_shelf: data.number_shelf,
        username: user.username,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/consumables/list`)
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
            <CustomTextField
              label='Количество'
              placeholder='Укажите количество'
              name='quantity'
              control={control}
              width={'30%'}
              type='number'
            />
            <CustomTextField
              label='Номер стеллажа'
              placeholder='Укажите стеллаж'
              name='number_rack'
              control={control}
              width={'30%'}
              type='number'
            />
            <CustomTextField
              label='Номер полки'
              placeholder='Укажите полку'
              name='number_shelf'
              control={control}
              width={'30%'}
              type='number'
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
                <Button variant='contained' component={Link} to={`/consumables/list`}>
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
