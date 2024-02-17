import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios";
import {Link} from "react-router-dom";
import {IconButton, MenuItem,} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar";
import MaterialReactTableList from "../../Tables/MaterialReactTableList";


const ListEmployee = () => {
    const [empl, setEmpls] = useState()
    const [loading, setLoading] = useState(true)

    const GetData = useCallback(async () => {
         await AxiosInstanse.get(`employee/employee_list/`).then((res) => {
            setEmpls(res.data)
            setLoading(false)
        })
    })

    useEffect(() =>{
        GetData();
    },[])

    const columns = useMemo(() => [
        {
            accessorFn: (row) => `${row.surname} ${row.name} ${row.last_name}`,
            header: 'Сотрудник',

        },
        {
            accessorKey: 'post.name',
            header: 'Должность',
        },
        {
            accessorKey: 'post.departament.name',
            header: 'Отдел',
        },
        {
            accessorKey: 'employeeEmail',
            header: 'E-mail',
        },
        {
            accessorKey: 'workplace.name',
            header: 'Рабочее место',
        },
                {
            accessorKey: 'workplace.room.name',
            header: 'Кабинет',
        },
        {
            accessorKey: 'workplace.room.building',
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
                    data={empl}
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

export default ListEmployee