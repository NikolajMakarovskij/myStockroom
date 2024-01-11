import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar";
import MaterialReactTableList from "../../Tables/MaterialReactTableList";


const ListRoom = () => {

    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)
    const GetData = useCallback( async () => {
        await AxiosInstanse.get(`workplace/api/v1/room/`).then((res) => {
            setRooms(res.data)
            setLoading(false)
        })
    })

    useEffect(() =>{
        GetData();
    },[])

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