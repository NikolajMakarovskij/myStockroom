import { React, useState, useEffect, useCallback } from 'react'
import { Box, Button, Typography } from '@mui/material'
import { useForm } from 'react-hook-form'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import AxiosInstanse from '../../Axios'
import { useNavigate, useParams, Link } from 'react-router-dom'
import PrintError from '../../Errors/Error'
import useCSRF from '../../Hooks/CSRF'
import LinearIndeterminate from '../../appHome/ProgressBar'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function RemoveFromStockConsumable() {
  const CSRF = useCSRF()
  const conParam = useParams()
  const conId = conParam.stock_model
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
    username: '',
  }

  const submission = useCallback(() => {
    AxiosInstanse.post(
      `stockroom/remove_from_stock_consumable/`,
      {
        model_id: conId,
        username: user.username,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/stock/consumables/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })

  const { handleSubmit } = useForm({ defaultValues: defaultValues })

  return (
    <form onSubmit={handleSubmit(submission)}>
      <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
        <Typography>Удалить расходник со склада?</Typography>
      </Box>
      {loading ? (
        <LinearIndeterminate />
      ) : error ? (
        <PrintError error={error} />
      ) : (
        <Box sx={{ display: 'flex', width: '100%', boxShadow: 3, padding: 4, flexDirection: 'column' }}>
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
                  Да
                </Button>
                <Button variant='contained' component={Link} to={`/stock/consumables/list`}>
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
