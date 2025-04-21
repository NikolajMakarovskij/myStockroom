import { React, useMemo, useState } from 'react'
import AxiosInstanse from '../../Axios'
import { Box } from '@mui/material'
import LinearIndeterminate from '../../appHome/ProgressBar'
import MaterialReactTableTabsList from '../../Tables/MaterialReactTableTabsList'
import useInterval from '../../Hooks/useInterval'
import PrintError from '../../Errors/Error'
import DialogConsumableDetail from '../Consumables/DialogConsumableDetail'

const ListConsumptionConsumables = () => {
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
        await AxiosInstanse.get(`/stockroom/consumption_con_list/`).then((res) => {
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
        await AxiosInstanse.get(`/consumables/consumable_category/`).then((res) => {
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
        accessorFn: ``,
        header: 'Расходник',
        // eslint-disable-next-line react/prop-types
        Cell: ({ renderedCellValue, row }) => (
          <Box>
            <DialogConsumableDetail
              // eslint-disable-next-line react/prop-types
              consumable={row.original.name}
              // eslint-disable-next-line react/prop-types
              id={row.original.stock_model_id}
            />

            <span>{renderedCellValue}</span>
          </Box>
        ),
      },
      {
        accessorKey: 'device_name',
        header: 'Устройство',
      },
      {
        accessorKey: 'device_count',
        header: 'Количество устройств',
      },
      {
        accessorKey: 'quantity_all',
        header: 'Расход за все время',
      },
      {
        accessorKey: 'quantity_last_year',
        header: 'Расход за прошлый год',
      },
      {
        accessorKey: 'quantity_current_year',
        header: 'Расход за текущий год',
      },
      {
        accessorKey: 'quantity',
        header: 'Количество на складе',
      },
      {
        accessorKey: 'requirement',
        header: 'Потребность',
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
        <MaterialReactTableTabsList columns={columns} data={consumable} category={category} />
      )}
    </>
  )
}

export default ListConsumptionConsumables
