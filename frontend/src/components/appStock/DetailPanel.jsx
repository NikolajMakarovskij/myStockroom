import PrintError from '../Errors/Error'
import { useState, useCallback, useEffect } from 'react'
import LinearIndeterminate from '../appHome/ProgressBar'
import AxiosInstanse from '../Axios'
import DialogDeviceDetail from './Devices/DialogDeviceDetail'
import { Typography, Box, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material'

export default function DetailPanel({ row, link }) {
  const [history, setHistory] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState(null)

  const GetData = useCallback(async () => {
    try {
      await AxiosInstanse(`${link}${row}/`).then((res) => {
        setHistory(res.data)
      })
    } catch (error) {
      setError(error.message)
    } finally {
      setIsLoading(false)
    }
  })

  useEffect(() => {
    GetData()
  }, [])

  console.log(history)
  if (isLoading)
    return (
      <Box mt={1.25}>
        <LinearIndeterminate />
      </Box>
    )
  if (error) return <PrintError error={error} />
  if (history.length === 0)
    return (
      <Typography sx={{ mt: 1.5, pt: 0.5, pb: 0.5, textAlign: 'center' }} component={Paper}>
        История не обнаружена
      </Typography>
    )

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Название</TableCell>
            <TableCell>Количество</TableCell>
            <TableCell>Дата последней установки</TableCell>
            <TableCell>Статус</TableCell>
            <TableCell>Примечание</TableCell>
            <TableCell>Пользователь</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {history.map((item, index) => (
            <TableRow key={index}>
              <TableCell>{item.stock_model}</TableCell>
              <TableCell>{item.quantity}</TableCell>
              <TableCell>{item.dateInstall}</TableCell>
              <TableCell>
                <Box>
                  {
                    // eslint-disable-next-line react/prop-types
                    item.device ? (
                      <DialogDeviceDetail
                        // eslint-disable-next-line react/prop-types
                        status={item.status}
                        // eslint-disable-next-line react/prop-types
                        device={item.device}
                        // eslint-disable-next-line react/prop-types
                        id={item.deviceId}
                      />
                    ) : (
                      // eslint-disable-next-line react/prop-types
                      item.status
                    )
                  }
                </Box>
              </TableCell>
              <TableCell>{item.note}</TableCell>
              <TableCell>{item.user}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  )
}
