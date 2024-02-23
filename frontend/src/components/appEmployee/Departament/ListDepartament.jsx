import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar";
import MaterialReactTableList from "../../Tables/MaterialReactTableList";
import useInterval from "../../Hooks/useInterval"
import PrintError from "../../Errors/Error";


const ListDepartament = () => {

    const [dep, setDeps] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [delay, setDelay] = useState(100)

    useInterval(() => {

        async function getData() {
            try {
                await AxiosInstanse.get(`employee/departament/`).then((res) => {
                    setDeps(res.data)
                    setLoading(false)
                    setError(null)
                    setDelay(5000)
                })
              } catch (error) {
                    setError(error.message);
                    setDelay(null)
              } finally {
                    setLoading(false);
              }
        }
        getData();
    }, delay);

    const columns = useMemo(() => [
        {
            accessorKey: 'name', //access nested data with dot notation
            header: 'Отдел',
        },
    ],
        [],
    );

    return(
        <>
            {loading ? <LinearIndeterminate/> :
                error ? <PrintError error={error}/>:
                    <MaterialReactTableList
                        columns={columns}
                        data={dep}
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

export default ListDepartament