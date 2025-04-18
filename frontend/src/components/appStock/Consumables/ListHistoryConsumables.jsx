import { React, useMemo, useState } from 'react'
import AxiosInstanse from '../../Axios'
import { Link } from 'react-router-dom'
import { IconButton, MenuItem } from '@mui/material'
//import { Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material'
import LinearIndeterminate from '../../appHome/ProgressBar'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'
import useInterval from '../../Hooks/useInterval'
import PrintError from '../../Errors/Error'

const ListHistoryConsumables = () => {
  const [consumable, setConsumables] = useState()
  const [category, setCategory] = useState('')
  const [loadingConsumables, setLoadingConsumables] = useState(true)
  const [loadingCategory, setLoadingCategory] = useState(true)
  const [errorConsumables, setErrorConsumables] = useState(false)
  const [errorCategory, setErrorCategory] = useState(false)
  const [delay, setDelay] = useState(100)

  useInterval(() => {
    async function getConsumables() {
      try {
        await AxiosInstanse.get(`/stockroom/history_con_list/`).then((res) => {
          setConsumables(res.data)
          setErrorConsumables(null)
          setDelay(5000)
        })
      } catch (error) {
        setErrorConsumables(error.message)
        setDelay(null)
      } finally {
        setLoadingConsumables(false)
      }
    }
    async function getCategory() {
      try {
        await AxiosInstanse.get(`/stockroom/stock_con_cat_list/`).then((res) => {
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
    Promise.all([getCategory(), getConsumables()])
  }, delay)

  const columns = useMemo(
    () => [
      {
        accessorKey: 'stock_model',
        header: 'Расходник',
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
        accessorFn: (row) => (row.device ? `${row.status} на устройство  ${row.device}` : `${row.status}`),
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
      ) : loadingConsumables ? (
        <LinearIndeterminate />
      ) : errorConsumables ? (
        <PrintError error={errorConsumables} />
      ) : (
        <MaterialReactTableTabsList
          columns={columns}
          data={consumable}
          category={category}
          renderRowActionMenuItems={({
            //row,
            menuActions = [
              //{ name: 'Добавить', path: `create`, icon: <AddIcon />, color: 'success' },
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

export default ListHistoryConsumables
