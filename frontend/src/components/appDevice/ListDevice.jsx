import {React, useEffect, useMemo, useState, useCallback} from 'react'
import {
    MaterialReactTable,
} from 'material-react-table';
//import {createTheme} from "@mui/material/styles";
import AxiosInstanse from "../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem,} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import {MRT_Localization_RU} from 'material-react-table/locales/ru';
import LinearIndeterminate from "../appHome/ProgressBar";

/*const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});*/

const ListDevice = () => {
    const [device, setDevices] = useState()
    const [loading, setLoading] = useState(true)

    const GetData = useCallback(async () => {
         await AxiosInstanse.get(`device/api/v1/device_list/`, {timeout: 1000*30}).then((res) => {
            setDevices(res.data)
            setLoading(false)
        })
    })

    useEffect(() =>{
        GetData();
    },[])

    const columns = useMemo(() => [
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
    );

    return(
        <div>
            {loading ? <LinearIndeterminate/> :
                <MaterialReactTable
                    columns={columns}
                    data={device}
                    localization={MRT_Localization_RU}
                    enableColumnResizing={true}
                    positionPagination='both'
                    enableRowNumbers='true'
                    enableRowVirtualization='true'
                    enableRowActions
                    renderRowActionMenuItems={({
                        row,
                        menuActions = [
                            //{'name': 'Добавить', 'path': `create`, 'icon': <AddIcon/>, 'color': 'success',},
                            //{'name': 'Редактировать', 'path': `edit/${row.original.id}`, 'icon': <EditIcon/>, 'color': 'primary',},
                            //{'name': 'Удалить', 'path': `remove/${row.original.id}`, 'icon': <DeleteIcon/>, 'color': 'error',},
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

export default ListDevice