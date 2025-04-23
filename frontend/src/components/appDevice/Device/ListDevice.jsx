import { React, useMemo, useState } from 'react'
import AxiosInstanse from '../../Axios.jsx'
import { Link } from 'react-router-dom'
import {
  IconButton,
  MenuItem,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material'
import { Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material'
import LinearIndeterminate from '../../appHome/ProgressBar.jsx'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList.jsx'
import { TreeItem, SimpleTreeView } from '@mui/x-tree-view'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import ChevronRightIcon from '@mui/icons-material/ChevronRight'
import useInterval from '../../Hooks/useInterval'
import PrintError from '../../Errors/Error'

const ListDevice = () => {
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
        await AxiosInstanse.get(`/devices/device_list/`, { timeout: 1000 * 30 }).then((res) => {
          setDevices(res.data)
          setError(null)
          setDelay(5000)
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
        await AxiosInstanse.get(`/devices/device_cat/`).then((res) => {
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
    Promise.all([getCategory(), getDevices()])
  }, delay)

  const columns = useMemo(
    () => [
      {
        accessorKey: 'accounting',
        header: '',
      },
      {
        accessorKey: 'name',
        header: 'Устройство',
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
        accessorKey: 'hostname',
        header: 'Хост',
      },
      {
        accessorKey: 'ip_address',
        header: 'ip',
      },
      {
        accessorKey: 'serial',
        header: 'Серийный №',
      },
      {
        accessorKey: 'invent',
        header: 'Инвентарный №',
      },
      {
        accessorKey: 'workplace.name',
        header: 'Рабочее место',
      },
      {
        accessorKey: 'workplace.room.building',
        header: 'Здание',
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
              { name: 'Добавить', path: `create`, icon: <AddIcon />, color: 'success' },
              { name: 'Редактировать', path: `edit/${row.original.id}`, icon: <EditIcon />, color: 'primary' },
              { name: 'Удалить', path: `remove/${row.original.id}`, icon: <DeleteIcon />, color: 'error' },
              {
                name: 'Установить расходник',
                path: `add_consumable/${row.original.id}`,
                icon: <AddIcon />,
                color: 'info',
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
                {row.original.consumable.length == 0 ? (
                  <></>
                ) : (
                  <TreeItem itemId='1' label='Расходники'>
                    <TableContainer component={Paper}>
                      <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Название</TableCell>
                            <TableCell>Описание</TableCell>
                            <TableCell>Количество</TableCell>
                            <TableCell>Разность</TableCell>
                            <TableCell>Примечание</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          {row.original.consumable.map((item, index) => (
                            <TableRow key={index}>
                              <TableCell>{item.name}</TableCell>
                              <TableCell>{item.description}</TableCell>
                              <TableCell>{item.quantity}</TableCell>
                              <TableCell>{item.difference}</TableCell>
                              <TableCell>{item.note}</TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    </TableContainer>
                  </TreeItem>
                )}
                {row.original.accessories.length == 0 ? (
                  <></>
                ) : (
                  <TreeItem itemId='2' label='Комплектующие'>
                    <TableContainer component={Paper}>
                      <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Название</TableCell>
                            <TableCell>Описание</TableCell>
                            <TableCell>Количество</TableCell>
                            <TableCell>Разность</TableCell>
                            <TableCell>Примечание</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          {row.original.accessories.map((item, index) => (
                            <TableRow key={index}>
                              <TableCell>{item.name}</TableCell>
                              <TableCell>{item.description}</TableCell>
                              <TableCell>{item.quantity}</TableCell>
                              <TableCell>{item.difference}</TableCell>
                              <TableCell>{item.note}</TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    </TableContainer>
                  </TreeItem>
                )}
                {/*<TreeItem nodeId="3" label="История использования">
                                    <TableContainer component={Paper}>
                                        <Table>
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell >Количество</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                <TableRow>
                                                    <TableCell>{row.original.id}</TableCell>
                                                </TableRow>
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                                </TreeItem>*/}
              </SimpleTreeView>
            ) : null
          }
        />
      )}
    </>
  )
}

export default ListDevice
