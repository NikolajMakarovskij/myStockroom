import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar";
import MaterialReactTableList from "../../Tables/MaterialReactTableList";
import useInterval from "../../Hooks/useInterval"
import PrintError from "../../Errors/Error";


const ListRoom = () => {

    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [delay, setDelay] = useState(100)

    useInterval(() => {

        async function fetchData() {
            try {
                await AxiosInstanse.get(`workplace/room/`).then((res) => {
                    setRooms(res.data)
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
        fetchData();
    }, delay);

    const columns = useMemo(() => [
        {
            accessorKey: 'name', //access nested data with dot notation
            header: 'Кабинет',
        },
        {
            accessorKey: 'floor',
            header: 'Этаж',
        },
        {
            accessorKey: 'building',
            header: 'Здание',
        },
    ],
        [],
    );

    return(
        <>
            {loading ? <LinearIndeterminate/> :
                error ? <PrintError error={error}/> :
                <MaterialReactTableList
                    columns={columns}
                    data={room}
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

export default ListRoom