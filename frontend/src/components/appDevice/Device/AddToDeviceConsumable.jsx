import { React, useState, useEffect, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import CustomTextField from '../../Forms/TextField.jsx'
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

export default function AddToDeviceConsumable() {
  const CSRF = useCSRF()
  const deviceParam = useParams()
  const deviceId = deviceParam.id
  const [user, setUser] = useState(null)
  const [consumable, setConsumable] = useState(null)
  const [errorEdit, setErrorEdit] = useState(null)
  const [loading, setLoading] = useState(true)
  const [loadingCons, setLoadingCons] = useState(true)
  const [error, setError] = useState(null)
  const [errorCons, setErrorCons] = useState(null)
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

  const GetDevice = useCallback(async () => {
    try {
      await AxiosInstanse.get(`devices/device_list/${deviceId}/`).then((res) => {
        setConsumable(res.data.consumable)
      })
    } catch (error) {
      setErrorCons(error.message)
    } finally {
      setLoadingCons(false)
    }
  })

  useEffect(() => {
    Promise.all([GetUser(), GetDevice()])
  }, [])

  const defaultValues = {
    model_id: '',
    device: '',
    quantity: '',
    note: '',
    username: '',
  }

  const schema = yup
    .object({
      model_id: yup.string().required('Обязательное поле'),
      quantity: yup.number('Введите целое число').integer('Введите целое число').required('Обязательное поле'),
      note: yup.string().max(1000, 'Должно быть короче 1000 символов').required('Обязательное поле'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `stockroom/add_to_device_consumable/`,
      {
        model_id: data.model_id,
        device: deviceId,
        quantity: data.quantity,
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
      {loading && loadingCons ? (
        <LinearIndeterminate />
      ) : error ? (
        <PrintError error={error} />
      ) : (
        <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
          <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
            <AutocompleteField
              loading={loadingCons}
              error={errorCons}
              name='model_id'
              id='model_id'
              control={control}
              width={'30%'}
              options={consumable}
              label='Выберите расходник'
              placeholder='Выберите расходник'
              noOptionsText='Расходник не обнаружен'
              optionLabel={(option) => `${option.name}`}
            />
            <CustomTextField
              label='Количество'
              placeholder='Укажите количество'
              name='quantity'
              control={control}
              width={'30%'}
              type='number'
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
