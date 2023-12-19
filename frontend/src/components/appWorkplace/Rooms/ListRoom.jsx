import {React, useEffect, useMemo, useState,} from 'react'
import {
    MaterialReactTable,
} from 'material-react-table';
import {createTheme, ThemeProvider} from "@mui/material/styles";
import AxiosInstanse from "../../Axios";
import {useNavigate, Link} from "react-router-dom";
import {IconButton, MenuItem, Box} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon, Print as PrintIcon } from '@mui/icons-material';
import {MRT_Localization_RU} from 'material-react-table/locales/ru';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const ListRoom = () => {

    const [room, setRooms] = useState()
    const [loading, setLoading] = useState(true)
    const menuActions = [
        {'name': 'Добавить', 'path': `create`, 'icon': <AddIcon/>, 'color': 'primary',},
        {'name': 'Редактировать', 'path': `edit/`, 'icon': <EditIcon/>, 'color': 'primary',},
        {'name': 'Удалить', 'path': 'delete', 'icon': <DeleteIcon/>, 'color': 'error',},
    ]
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
            {loading ? <p>Загрузка данных...</p> :
                <MaterialReactTable
                    columns={columns}
                    data={room}
                    localization={MRT_Localization_RU}
                    positionPagination='both'
                    enableRowNumbers='true'
                    enableRowVirtualization='true'
                    enableRowActions
                    renderRowActionMenuItems={({ row }) => [
                        /*menuActions.map(
                            (item, index) => (
                            <MenuItem key={index} component={Link} to={item.path}>
                                <IconButton color={item.color} >
                                    {item.icon}
                                </IconButton>
                                {item.name}
                            </MenuItem>
                        ))*/
                        <MenuItem key='create' component={Link} to={`create`}>
                            <IconButton color='primary' >
                                <AddIcon/>
                            </IconButton>
                            Создать
                        </MenuItem>,
                        <MenuItem key='edit' component={Link} to={`edit/${row.original.id}`}>
                            <IconButton color='primary' >
                                <EditIcon/>
                            </IconButton>
                            Редактировать
                        </MenuItem>


                    ]}
                    /*renderToolbarInternalActions={() => (
                        <Box>
                            <IconButton
                              onClick={() => {
                                window.print();
                              }}
                            >
                              <PrintIcon />
                            </IconButton>
                        </Box>
                    )}*/
                />
            }

        </div>
    )



};

export default ListRoom