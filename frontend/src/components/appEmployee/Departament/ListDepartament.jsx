import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar";
import MaterialReactTableList from "../../Tables/MaterialReactTableList";


const ListDepartament = () => {

    const [dep, setDeps] = useState()
    const [loading, setLoading] = useState(true)
    const GetData = useCallback( async () => {
        await AxiosInstanse.get(`employee/departament/`).then((res) => {
            setDeps(res.data)
            setLoading(false)
        })
    })

    useEffect(() =>{
        GetData();
    },[])

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