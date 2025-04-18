import { React, useEffect, useState, useCallback, Fragment } from 'react'
import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  IconButton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableRow,
} from '@mui/material'
import CloseIcon from '@mui/icons-material/Close'
import AxiosInstanse from '../../Axios'
import LinearIndeterminate from '../../appHome/ProgressBar'
import PrintError from '../../Errors/Error.jsx'
import PropTypes from 'prop-types'

export default function DialogDeviceDetail(props) {
  const { status, device, id } = props
  const [open, setOpen] = useState(false)
  const [detail, setDetail] = useState()
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  const GetData = useCallback(async () => {
    try {
      await AxiosInstanse.get(`devices/device_list/${id}/`).then((res) => {
        setDetail(res.data)
      })
    } catch (error) {
      setError(error.message)
    } finally {
      setLoading(false)
    }
  })

  useEffect(() => {
    GetData()
  })

  const handleClickOpen = () => {
    setOpen(true)
  }
  const handleClose = () => {
    setOpen(false)
  }

  return (
    <Fragment>
      <Button variant='outlined' onClick={handleClickOpen} style={{ textTransform: 'none' }}>
        {status} на устройство {device}
      </Button>
      <Dialog onClose={handleClose} fullWidth='true' maxWidth='sm' open={open}>
        <DialogTitle sx={{ m: 0, p: 2 }} id='customized-dialog-title'>
          {loading ? <LinearIndeterminate /> : error ? <PrintError error={error} /> : ` ${detail.name}`}
        </DialogTitle>
        <IconButton
          aria-label='close'
          onClick={handleClose}
          sx={(theme) => ({
            position: 'absolute',
            right: 8,
            top: 8,
            color: theme.palette.grey[500],
          })}
        >
          <CloseIcon />
        </IconButton>
        <DialogContent dividers>
          {loading ? (
            <LinearIndeterminate />
          ) : error ? (
            <PrintError error={error} />
          ) : (
            <TableContainer>
              <Table>
                <TableBody>
                  <TableRow>
                    <TableCell>Инв. №:</TableCell>
                    <TableCell>{detail.invent}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Сер. №:</TableCell>
                    <TableCell>{detail.serial}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Здание:</TableCell>
                    <TableCell>{detail.workplace.room.building}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Кабинет №:</TableCell>
                    <TableCell>{detail.workplace.room.name}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Хост:</TableCell>
                    <TableCell>{detail.hostname}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>IP:</TableCell>
                    <TableCell>{detail.ip_address}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Ресурс:</TableCell>
                    <TableCell>{detail.resource}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Описание:</TableCell>
                    <TableCell>{detail.description}</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>Примечание:</TableCell>
                    <TableCell>{detail.note}</TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </TableContainer>
          )}
        </DialogContent>
      </Dialog>
    </Fragment>
  )
}

DialogDeviceDetail.propTypes = {
  status: PropTypes.string,
  device: PropTypes.string,
  id: PropTypes.string,
}
