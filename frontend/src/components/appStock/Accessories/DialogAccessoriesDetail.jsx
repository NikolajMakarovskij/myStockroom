import { React, useEffect, useState, useCallback, Fragment } from 'react'
import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  IconButton,
  Table,
  TableHead,
  TableBody,
  TableCell,
  TableContainer,
  TableRow,
  Toolbar,
  Typography,
} from '@mui/material'
import CloseIcon from '@mui/icons-material/Close'
import AxiosInstanse from '../../Axios.jsx'
import LinearIndeterminate from '../../appHome/ProgressBar.jsx'
import PrintError from '../../Errors/Error.jsx'
import PropTypes from 'prop-types'

export default function DialogAccessoriesDetail(props) {
  const { consumable, id } = props
  const [open, setOpen] = useState(false)
  const [detail, setDetail] = useState()
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  const GetData = useCallback(async () => {
    try {
      await AxiosInstanse.get(`consumables/accessories_list/${id}/`).then((res) => {
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
      <Button variant='text' onClick={handleClickOpen} style={{ textTransform: 'none' }}>
        {consumable}
      </Button>
      <Dialog onClose={handleClose} fullWidth='true' maxWidth='sm' open={open}>
        <DialogTitle sx={{ m: 0, p: 2 }} id='accessories'>
          {loading ? <LinearIndeterminate /> : error ? <PrintError error={error} /> : `${detail.name}`}
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
          ) : detail.accessories.length == 0 ? (
            <Typography>На балансе нет</Typography>
          ) : (
            <TableContainer>
              <Toolbar>
                <Typography>Разность: {detail.difference}</Typography>
              </Toolbar>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>Название:</TableCell>
                    <TableCell>Счет:</TableCell>
                    <TableCell>Код:</TableCell>
                    <TableCell>Остаток:</TableCell>
                    <TableCell>Стоимость:</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {detail.consumable.map((item, index) => (
                    <TableRow key={index}>
                      <TableCell>{item.name}</TableCell>
                      <TableCell>{item.account}</TableCell>
                      <TableCell>{item.code}</TableCell>
                      <TableCell>{item.quantity}</TableCell>
                      <TableCell>{item.cost}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          )}
        </DialogContent>
      </Dialog>
    </Fragment>
  )
}

DialogAccessoriesDetail.propTypes = {
  consumable: PropTypes.string,
  id: PropTypes.string,
}
