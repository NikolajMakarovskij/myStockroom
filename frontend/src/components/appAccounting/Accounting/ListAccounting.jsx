import {React, useMemo, useState,} from 'react';
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {
    IconButton,
    MenuItem,
} from '@mui/material';
import { NumericFormat } from 'react-number-format';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar";
import MaterialReactTableTabsList from "../../Tables/MaterialReactTableTabsList";
import useInterval from "../../Hooks/useInterval";
import PrintError from "../../Errors/Error";


const ListAccounting = () => {
    const [accounting, setAccounting] = useState()
    const [category, setCategory] = useState('')
    const [loadingAccounting, setLoadingAccounting] = useState(true)
    const [loadingCategory, setLoadingCategory] = useState(true)
    const [errorAccounting, setErrorAccounting] = useState(false)
    const [errorCategory, setErrorCategory] = useState(false)
    const [delay, setDelay] = useState(100)



    useInterval(() => {
        async function getAccounting() {
            try {
                await AxiosInstanse.get(`/accounting/accounting_list/`).then((res) => {
                    setAccounting(res.data)
                    setErrorAccounting(null)
                    setDelay(5000)
                })
              } catch (error) {
                    setErrorAccounting(error.message);
                    setDelay(null)
              } finally {
                    setLoadingAccounting(false);
              }
        }
        async function getCategory() {
            try {
                await AxiosInstanse.get(`/accounting/accounting_category/`).then((res) => {
                    setCategory(res.data)
                    setErrorCategory(null)
                    setDelay(5000)
                })
              } catch (error) {
                    setErrorCategory(error.message);
                    setDelay(null)
              } finally {
                    setLoadingCategory(false);
              }
        }
        Promise.all([getCategory(), getAccounting()])
    }, delay);

    const columns = useMemo(() => [
        {
            accessorKey: 'name',
            header: 'Название',
        },
        {
            accessorKey: 'account',
            header: 'Счет',
        },
        {
            accessorKey: 'code',
            header: 'Код',
        },
        {
            accessorKey: 'quantity',
            header: 'Количество',
        },
        {
            accessorKey: `cost`,
            header: 'Стоимость',
            Cell: ({renderCellValue, row}) => (
                <NumericFormat
                    value={row.original.cost}
                    displayType={"text"}
                    decimalSeparator=","
                    thousandSeparator=" "
                    fixedDecimalScale
                    suffix={' \u20bd'}
                />
            ),
        },
        {
            accessorKey: 'costAll',
            header: 'Общая стоимость',
            Cell: ({renderCellValue, row}) => (
                <NumericFormat
                    value={row.original.costAll}
                    displayType={"text"}
                    decimalSeparator=","
                    thousandSeparator=" "
                    fixedDecimalScale
                    suffix={' \u20bd'}
                />
            ),
        },
        {
            accessorKey: 'note',
            header: 'Примечание',
        }
    ],
        [],
    );

    return(
        <>
            {loadingCategory ? <LinearIndeterminate/> :
                errorCategory ? <PrintError error={errorCategory}/> :
                    loadingAccounting ? <LinearIndeterminate/> :
                        errorAccounting ? <PrintError error={errorAccounting}/> :
            <MaterialReactTableTabsList
                columns={columns}
                data={accounting}
                category={category}
                renderRowActionMenuItems={({
                        row,
                        menuActions = [
                            {'name': 'Добавить', 'path': `create`, 'icon': <AddIcon/>, 'color': 'success',},
                            {'name': 'Редактировать', 'path': `edit/${row.original.id}`, 'icon': <EditIcon/>, 'color': 'primary',},
                            {'name': 'Удалить', 'path': `remove/${row.original.id}`, 'icon': <DeleteIcon/>, 'color': 'error',},
                        ], }) => [
                        menuActions.map(
                            (item, index) => (
                            <MenuItem key={index} component={Link} to={item.path}>
                                <IconButton color={item.color} >
                                    {item.icon}
                                </IconButton>
                                {item.name}
                            </MenuItem>
                        ))
                    ]}
                />
            }
        </>
    )



};

export default ListAccounting