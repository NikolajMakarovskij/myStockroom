import { React, useMemo, useState, useCallback, useEffect } from 'react'
import AxiosInstanse from '../../Axios'
import { Link } from 'react-router-dom'
import { IconButton, MenuItem } from '@mui/material'
//import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from '../../appHome/ProgressBar.jsx'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'

export default function ListStockDevices() {
  const [device, setDevices] = useState()
  const [category, setCategory] = useState('')
  const [loading, setLoading] = useState(true)

  const GetData = useCallback(async () => {
    await AxiosInstanse.get(`stockroom/stock_dev_list/`, { timeout: 1000 * 30 }).then((res) => {
      setDevices(res.data)
    })
    await AxiosInstanse.get(`stockroom/stock_dev_cat/`).then((res) => {
      setCategory(res.data)
      setLoading(false)
    })
  })

  useEffect(() => {
    GetData()
  }, [])

  const columns = useMemo(
    () => [
      {
        id: 'stock_model',
        accessorKey: 'stock_model.name',
        header: 'Устройство',
      },
      {
        accessorKey: 'stock_model.description',
        header: 'Описание',
      },
      {
        accessorKey: 'stock_model.note',
        header: 'Примечание',
      },
      {
        accessorKey: 'stock_model.quantity',
        header: 'Количество',
      },
      {
        accessorKey: 'stock_model.serial',
        header: 'Серийный №',
      },
      {
        accessorKey: 'stock_model.invent',
        header: 'Инвентарный №',
      },
      {
        accessorKey: 'rack',
        header: 'Стеллаж',
      },
      {
        accessorKey: 'shelf',
        header: 'Полка',
      },
      {
        accessorKey: 'stock_model.workplace.name',
        header: 'Рабочее место',
      },
      {
        accessorKey: 'stock_model.workplace.room.building',
        header: 'Здание',
      },
      {
        accessorKey: 'categories.name',
        header: 'Группа',
      },
      {
        accessorKey: 'dateAddToStock',
        header: 'Приход',
      },
      {
        accessorKey: 'dateInstall',
        header: 'Установка',
      },
    ],
    [],
  )

  return (
    <>
      {loading ? (
        <LinearIndeterminate />
      ) : (
        <>
          <MaterialReactTableTabsList
            columns={columns}
            data={device}
            category={category}
            renderRowActionMenuItems={({
              //row,
              menuActions = [
                //{'name': 'Добавить', 'path': `create`, 'icon': <AddIcon/>, 'color': 'success',},
                //{'name': 'Редактировать', 'path': `edit/${row.original.id}`, 'icon': <EditIcon/>, 'color': 'primary',},
                //{'name': 'Удалить', 'path': `remove/${row.original.id}`, 'icon': <DeleteIcon/>, 'color': 'error',},
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
        </>
      )}
    </>
  )
}
