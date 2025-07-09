import { React, useMemo, useState } from 'react'
import AxiosInstanse from '../../Axios'
import { Link } from 'react-router-dom'
import { IconButton, MenuItem } from '@mui/material'
import { Add as AddIcon, Delete as DeleteIcon } from '@mui/icons-material'
import { TreeItem, SimpleTreeView } from '@mui/x-tree-view'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import ChevronRightIcon from '@mui/icons-material/ChevronRight'
import LinearIndeterminate from '../../appHome/ProgressBar.jsx'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'
import useInterval from '../../Hooks/useInterval.jsx'
import PrintError from '../../Errors/Error.jsx'
import DetailPanel from '../../appStock/DetailPanel'

export default function ListStockDevices() {
  const [device, setDevices] = useState()
  const [category, setCategory] = useState('')
  const [loading, setLoading] = useState(true)
  const [loadingCategory, setLoadingCategory] = useState(true)
  const [error, setError] = useState(false)
  const [errorCategory, setErrorCategory] = useState(false)
  const [delay, setDelay] = useState(100)

  useInterval(() => {
    async function getDevices() {
      try {
        await AxiosInstanse.get(`stockroom/stock_dev_list/`).then((res) => {
          setDevices(res.data)
          setError(null)
          setDelay(30000)
        })
      } catch (error) {
        setError(error.message)
        setDelay(null)
      } finally {
        setLoading(false)
      }
    }
    async function getCategory() {
      try {
        await AxiosInstanse.get(`stockroom/stock_dev_cat_list/`).then((res) => {
          setCategory(res.data)
          setErrorCategory(null)
          setDelay(30000)
        })
      } catch (error) {
        setErrorCategory(error.message)
        setDelay(null)
      } finally {
        setLoadingCategory(false)
      }
    }
    Promise.all([getCategory(), getDevices()])
  }, delay)

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
      {loadingCategory ? (
        <LinearIndeterminate />
      ) : errorCategory ? (
        <PrintError error={errorCategory} />
      ) : loading ? (
        <LinearIndeterminate />
      ) : error ? (
        <PrintError error={error} />
      ) : (
        <MaterialReactTableTabsList
          columns={columns}
          data={device}
          category={category}
          renderRowActionMenuItems={({
            row,
            menuActions = [
              {
                name: 'Списать',
                path: `add_to_decommission/${row.original.stock_model.id}`,
                icon: <AddIcon />,
                color: 'secondary',
              },
              {
                name: 'Удалить',
                path: `remove_from_stock/${row.original.stock_model.id}`,
                icon: <DeleteIcon />,
                color: 'error',
              },
            ],
          }) => [
            menuActions.map((item, index) => (
              <MenuItem key={index} component={Link} to={item.path}>
                <IconButton color={item.color}>{item.icon}</IconButton>
                {item.name}
              </MenuItem>
            )),
          ]}
          renderDetailPanel={({ row }) =>
            row.original ? (
              <SimpleTreeView
                sx={{ width: '100%' }}
                defaultCollapseIcon={<ExpandMoreIcon />}
                defaultExpandIcon={<ChevronRightIcon />}
              >
                <TreeItem itemId='1' label='История использования устройства'>
                  <DetailPanel row={row.original.stock_model.id} link='/stockroom/history_dev_list/filter/' />
                </TreeItem>
              </SimpleTreeView>
            ) : null
          }
        />
      )}
    </>
  )
}
