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
  Paper,
} from '@mui/material'
import { NumericFormat } from 'react-number-format'
import { SimpleTreeView, TreeItem } from '@mui/x-tree-view'
import { Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import ChevronRightIcon from '@mui/icons-material/ChevronRight'
import LinearIndeterminate from '../../appHome/ProgressBar'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'
import useInterval from '../../Hooks/useInterval'
import PrintError from '../../Errors/Error'
import DetailPanel from '../../appStock/DetailPanel'

export default function ListAccessories() {
  const [accessories, setAccessories] = useState()
  const [category, setCategory] = useState('')
  const [loadingAccessories, setLoadingAccessories] = useState(true)
  const [loadingCategory, setLoadingCategory] = useState(true)
  const [errorAccessories, setErrorAccessories] = useState(false)
  const [errorCategory, setErrorCategory] = useState(false)
  const [delay, setDelay] = useState(100)

  useInterval(() => {
    async function getAccessories() {
      try {
        await AxiosInstanse.get(`/consumables/accessories_list/`).then((res) => {
          setAccessories(res.data)
          setErrorAccessories(null)
          setDelay(30000)
        })
      } catch (error) {
        setErrorAccessories(error.message)
        setDelay(null)
      } finally {
        setLoadingAccessories(false)
      }
    }
    async function getCategory() {
      try {
        await AxiosInstanse.get(`/consumables/accessories_category/`).then((res) => {
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
    Promise.all([getCategory(), getAccessories()])
  }, delay)

  const columns = useMemo(
    () => [
      {
        accessorKey: 'name',
        header: 'Комплктующее',
      },
      {
        accessorKey: 'description',
        header: 'Описание',
      },
      {
        accessorKey: 'note',
        header: 'Примечание',
      },
      {
        accessorKey: 'quantity',
        header: 'Количество',
      },
      {
        accessorKey: 'difference',
        header: 'Разность',
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
      ) : loadingAccessories ? (
        <LinearIndeterminate />
      ) : errorAccessories ? (
        <PrintError error={errorAccessories} />
      ) : (
        <MaterialReactTableTabsList
          columns={columns}
          data={accessories}
          category={category}
          renderRowActionMenuItems={({
            row,
            menuActions = [
              { name: 'Добавить', path: `create`, icon: <AddIcon />, color: 'success' },
              { name: 'Редактировать', path: `edit/${row.original.id}`, icon: <EditIcon />, color: 'primary' },
              { name: 'Удалить', path: `remove/${row.original.id}`, icon: <DeleteIcon />, color: 'error' },
              { name: 'Добавить на склад', path: `add_to_stock/${row.original.id}`, icon: <AddIcon />, color: 'info' },
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
                {row.original.accessories.length == 0 ? (
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
                          {row.original.accessories.map((item, index) => (
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
                {row.original.device.length == 0 ? (
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
                            <TableCell>{row.original.device.length}</TableCell>
                            <TableCell>
                              {row.original.device.map((item, index) => (
                                <TableRow key={index}>{item}</TableRow>
                              ))}
                            </TableCell>
                          </TableRow>
                        </TableBody>
                      </Table>
                    </TableContainer>
                  </TreeItem>
                )}
                <TreeItem itemId='3' label='История использования'>
                  <DetailPanel row={row.original.id} link='/stockroom/history_acc_list/filter/' />
                </TreeItem>
              </SimpleTreeView>
            ) : null
          }
        />
      )}
    </>
  )
}
