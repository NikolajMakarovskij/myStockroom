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
import PrintError from '../../Errors/Error'
import useCSRF from '../../Hooks/CSRF'
import MultilineField from '../../Forms/MultilineField'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function CreateAccounting() {
  const CSRF = useCSRF()
  const [cat, setCat] = useState()
  const [consumable, setConsumable] = useState()
  const [accessories, setAccessories] = useState()
  const [errorEdit, setErrorEdit] = useState(null)
  const [loadingCat, setLoadingCat] = useState(true)
  const [errorCat, setErrorCat] = useState(null)
  const [loadingConsumable, setLoadingConsumable] = useState(true)
  const [errorConsumable, setErrorConsumable] = useState(null)
  const [loadingAccessories, setLoadingAccessories] = useState(true)
  const [errorAccessories, setErrorAccessories] = useState(null)
  const [delay, setDelay] = useState(100)
  const navigate = useNavigate()

  useInterval(() => {
    async function getCategory() {
      try {
        await AxiosInstanse.get(`accounting/accounting_category/`).then((res) => {
          setCat(res.data)
          setErrorCat(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorCat(error.message)
        setDelay(null)
      } finally {
        setLoadingCat(false)
      }
    }
    async function getConsumable() {
      try {
        await AxiosInstanse.get(`consumables/consumable/`).then((res) => {
          setConsumable(res.data)
          setErrorConsumable(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorConsumable(error.message)
        setDelay(null)
      } finally {
        setLoadingConsumable(false)
      }
    }
    async function getAccessories() {
      try {
        await AxiosInstanse.get(`consumables/accessories/`).then((res) => {
          setAccessories(res.data)
          setErrorAccessories(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorAccessories(error.message)
        setDelay(null)
      } finally {
        setLoadingAccessories(false)
      }
    }
    Promise.all([getCategory(), getConsumable(), getAccessories()])
  }, delay)

  const defaultValues = {
    name: '',
    account: '',
    categories: '',
    consumable: '',
    accessories: '',
    code: '',
    quantity: 0,
    cost: 0,
    note: '',
  }

  const schema = yup
    .object({
      name: yup.string().required('Обязательное поле').max(500, 'Должно быть короче 500 символов'),
      account: yup.number().integer(),
      code: yup.string().max(50, 'Должно быть короче 50 символов'),
      quantity: yup.number().integer(),
      cost: yup.number(),
      note: yup.string().max(1000, 'Должно быть короче 1000 символов'),
    })
    .required()

  const { handleSubmit, control } = useForm({ defaultValues: defaultValues, resolver: yupResolver(schema) })

  const submission = useCallback((data) => {
    AxiosInstanse.post(
      `accounting/accounting/`,
      {
        name: data.name,
        account: data.account,
        categories: data.categories,
        consumable: data.consumable,
        accessories: data.accessories,
        code: data.code,
        quantity: data.quantity,
        cost: data.cost,
        note: data.note,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/accounting/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })
  return (
    <form onSubmit={handleSubmit(submission)}>
      <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
        <Typography>Добавить запись</Typography>
      </Box>
      <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
        <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
          <MultilineField
            label='Название'
            placeholder='Введите название'
            name='name'
            control={control}
            width={'30%'}
            rows={4}
            maxlength='500'
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
          <AutocompleteField
            loading={loadingCat}
            error={errorCat}
            name='categories'
            control={control}
            width={'30%'}
            options={cat}
            label='Выберите группу'
            placeholder='Выберите группу'
            noOptionsText='Группы не обнаружены'
            optionLabel={(option) => `${option.name}`}
          />
        </Box>
        <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
          <AutocompleteField
            loading={loadingConsumable}
            error={errorConsumable}
            name='consumable'
            control={control}
            width={'30%'}
            options={consumable}
            label='Выберите расходник'
            placeholder='Выберите расходник'
            noOptionsText='Расходники не обнаружены'
            optionLabel={(option) => `${option.name}`}
          />
          <AutocompleteField
            loading={loadingAccessories}
            error={errorAccessories}
            name='accessories'
            control={control}
            width={'30%'}
            options={accessories}
            label='Выберите комплектующее'
            placeholder='Выберите комплектующее'
            noOptionsText='Комплектующие не обнаружены'
            optionLabel={(option) => `${option.name}`}
          />
          <CustomTextField label='Счет' placeholder='Введите счет' name='account' control={control} width={'30%'} />
        </Box>
        <Box sx={{ display: 'flex', width: '100%', justifyContent: 'space-around', marginBottom: '40px' }}>
          <CustomTextField label='Код' placeholder='Введите код' name='code' control={control} width={'30%'} />
          <CustomTextField
            label='Количество'
            placeholder='Введите количество'
            name='quantity'
            control={control}
            width={'30%'}
          />
          <CustomTextField
            label='Стоимость'
            placeholder='Введите стоимость'
            name='cost'
            typy='number'
            control={control}
            width={'30%'}
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
              <Button variant='contained' component={Link} to={`/accounting/list`}>
                Отмена
              </Button>
            </Box>
          </ThemeProvider>
        </Box>
      </Box>
    </form>
  )
}
