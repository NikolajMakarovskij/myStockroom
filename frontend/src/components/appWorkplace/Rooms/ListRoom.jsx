import {React, useEffect, useMemo, useState,} from 'react'
import {
    MaterialReactTable,
} from 'material-react-table';
//import {createTheme} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import {MRT_Localization_RU} from 'material-react-table/locales/ru';
import LinearIndeterminate from "../../appHome/ProgressBar";
import BaseMRT from "../../appHome/BaseMRT";

/*const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});*/

const ListRoom = () => {

    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)
    const GetData = () => {
        AxiosInstanse.get(`workplace/api/v1/room/`).then((res) => {
            setRooms(res.data)
            setLoading(false)
        })
    }

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
        <div>
            {loading ? <LinearIndeterminate/> :
                <MaterialReactTable
                    columns={columns}
                    data={room}
                    localization={MRT_Localization_RU}
                    enableColumnResizing={true}
                    positionPagination='both'
                    enableRowNumbers='true'
                    enableRowVirtualization='true'
                    enableRowActions
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

        </div>
    )



};

export default ListRoom