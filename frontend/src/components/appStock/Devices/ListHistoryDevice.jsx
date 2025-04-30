import { React, useMemo, useState } from 'react'
import AxiosInstanse from '../../Axios'
import { Link } from 'react-router-dom'
import { IconButton, MenuItem } from '@mui/material'
import LinearIndeterminate from '../../appHome/ProgressBar'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'
import useInterval from '../../Hooks/useInterval'
import PrintError from '../../Errors/Error'

const ListHistoryDevice = () => {
  const [device, setDevice] = useState()
  const [category, setCategory] = useState('')
  const [loadingDevice, setLoadingDevice] = useState(true)
  const [loadingCategory, setLoadingCategory] = useState(true)
  const [errorDevice, setErrorDevice] = useState(false)
  const [errorCategory, setErrorCategory] = useState(false)
  const [delay, setDelay] = useState(100)

  useInterval(() => {
    async function getDevice() {
      try {
        await AxiosInstanse.get(`/stockroom/history_dev_list/`).then((res) => {
          setDevice(res.data)
          setErrorDevice(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorDevice(error.message)
        setDelay(null)
      } finally {
        setLoadingDevice(false)
      }
    }
    async function getCategory() {
      try {
        await AxiosInstanse.get(`/stockroom/stock_dev_cat_list/`).then((res) => {
          setCategory(res.data)
          setErrorCategory(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorCategory(error.message)
        setDelay(null)
      } finally {
        setLoadingCategory(false)
      }
    }
    Promise.all([getCategory(), getDevice()])
  }, delay)

  const columns = useMemo(
    () => [
      {
        accessorKey: `stock_model`,
        header: 'Устройство',
      },
      {
        accessorKey: 'categories.name',
        header: 'Группа',
      },
      {
        accessorKey: 'quantity',
        header: 'Количество',
      },
      {
        accessorKey: 'dateInstall',
        header: 'Дата последней установки',
      },
      {
        accessorKey: `status`,
        header: 'Статус',
      },
      {
        accessorKey: 'note',
        header: 'Примечание',
      },
      {
        accessorKey: 'user',
        header: 'Пользователь',
      },
    ],
    [],
  )

  return (
    <>
      {loadingCategory ? (
        <LinearIndeterminate />
      ) : errorCategory ? (
        <PrintError error={errorCategory} />
      ) : loadingDevice ? (
        <LinearIndeterminate />
      ) : errorDevice ? (
        <PrintError error={errorDevice} />
      ) : (
        <MaterialReactTableTabsList
          columns={columns}
          data={device}
          category={category}
          renderRowActionMenuItems={({
            //row,
            menuActions = [
              //{ name: 'Редактировать', path: `edit/${row.original.id}`, icon: <EditIcon />, color: 'primary' },
              //{ name: 'Удалить', path: `remove/${row.original.id}`, icon: <DeleteIcon />, color: 'error' },
            ],
          }) => [
            menuActions.map((item, index) => (
              <MenuItem key={index} component={Link} to={item.path}>
                <IconButton color={item.color}>{item.icon}</IconButton>
                {item.name}
              </MenuItem>
            )),
          ]}
        />
      )}
    </>
  )
}

export default ListHistoryDevice
