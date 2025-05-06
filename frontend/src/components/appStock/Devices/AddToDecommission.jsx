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

export default function AddToDecommission() {
  const CSRF = useCSRF()
  const deviceParam = useParams()
  const deviceId = deviceParam.stock_model
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
    device_id: '',
    username: '',
  }

  const { handleSubmit } = useForm({ defaultValues: defaultValues })

  const submission = useCallback(() => {
    AxiosInstanse.post(
      `decommission/add_to_decommission/`,
      {
        device_id: deviceId,
        username: user.username,
      },
      {
        headers: {
          'X-CSRFToken': CSRF,
        },
      },
    )
      .then(() => {
        navigate(`/decommission/list`)
      })
      .catch((error) => {
        setErrorEdit(error.response.data.detail)
      })
  })
  return (
    <form onSubmit={handleSubmit(submission)}>
      <Box sx={{ display: 'flex', justifyContent: 'center', width: '100%', marginBottom: '10px' }}>
        <Typography>Списать устройство</Typography>
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
                  Списать
                </Button>
                <Button variant='contained' component={Link} to={`/decommission/list`}>
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
