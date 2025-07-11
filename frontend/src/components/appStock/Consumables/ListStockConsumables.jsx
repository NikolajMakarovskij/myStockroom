import { React, useMemo, useState } from 'react'
import AxiosInstanse from '../../Axios'
import { Link } from 'react-router-dom'
import {
  IconButton,
  MenuItem,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper, //Typography
} from '@mui/material'
import { NumericFormat } from 'react-number-format'
import { SimpleTreeView, TreeItem } from '@mui/x-tree-view'
import { /*Edit as EditIcon, */ Delete as DeleteIcon } from '@mui/icons-material'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import ChevronRightIcon from '@mui/icons-material/ChevronRight'
import LinearIndeterminate from '../../appHome/ProgressBar'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'
import useInterval from '../../Hooks/useInterval'
import PrintError from '../../Errors/Error'

export default function ListStockConsumables() {
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
        await AxiosInstanse.get(`/stockroom/stock_con_list/`).then((res) => {
          setConsumables(res.data)
          setErrorConsumables(null)
          setDelay(30000)
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
          setDelay(30000)
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
        accessorKey: 'stock_model.name',
        header: 'Расходник',
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
        accessorKey: 'stock_model.quantity',
        header: 'Количество',
      },
      {
        accessorKey: 'stock_model.difference',
        header: 'Разность',
      },
      {
        accessorKey: 'dateAddToStock',
        header: 'Дата поступления',
      },
      {
        accessorKey: 'dateInstall',
        header: 'Дата последней установки',
      },
      {
        accessorKey: 'note',
        header: 'Примечание',
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
            row,
            menuActions = [
              //{ name: 'Редактировать', path: `edit/${row.original.id}`, icon: <EditIcon />, color: 'primary' },
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
            row.original.stock_model.consumable ? (
              <SimpleTreeView
                sx={{ width: '100%' }}
                defaultCollapseIcon={<ExpandMoreIcon />}
                defaultExpandIcon={<ChevronRightIcon />}
              >
                {row.original.stock_model.consumable.length == 0 ? (
                  <></>
                ) : (
                  <TreeItem itemId='1' label='На балансе'>
                    <TableContainer component={Paper}>
                      <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Название</TableCell>
                            <TableCell>Код</TableCell>
                            <TableCell>На балансе</TableCell>
                            <TableCell>Стоимость (1 шт.)</TableCell>
                            <TableCell>Общая cтоимость</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          {row.original.stock_model.consumable.map((item, index) => (
                            <TableRow key={index}>
                              <TableCell>{item.name}</TableCell>
                              <TableCell>{item.code}</TableCell>
                              <TableCell>{item.quantity}</TableCell>
                              <TableCell>
                                <NumericFormat
                                  value={item.cost}
                                  displayType={'text'}
                                  decimalSeparator=','
                                  thousandSeparator=' '
                                  fixedDecimalScale
                                  suffix={' \u20bd'}
                                />
                              </TableCell>
                              <TableCell>
                                <NumericFormat
                                  value={item.costAll}
                                  displayType={'text'}
                                  decimalSeparator=','
                                  thousandSeparator=' '
                                  fixedDecimalScale
                                  suffix={' \u20bd'}
                                />
                              </TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    </TableContainer>
                  </TreeItem>
                )}
                {row.original.stock_model.device.length == 0 ? (
                  <></>
                ) : (
                  <TreeItem itemId='2' label='Устройства'>
                    <TableContainer component={Paper}>
                      <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Количество</TableCell>
                            <TableCell>Устройства</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          <TableRow key='devices'>
                            <TableCell>{row.original.stock_model.device.length}</TableCell>
                            <TableCell>
                              {row.original.stock_model.device.map((item, index) => (
                                <TableRow key={index}>{item}</TableRow>
                              ))}
                            </TableCell>
                          </TableRow>
                        </TableBody>
                      </Table>
                    </TableContainer>
                  </TreeItem>
                )}
              </SimpleTreeView>
            ) : null
          }
        />
      )}
    </>
  )
}
