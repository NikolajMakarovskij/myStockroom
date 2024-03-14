import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios.jsx";
import {Link} from "react-router-dom";
import {IconButton, MenuItem,} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar.jsx";
import MaterialReactTableList from "../../Tables/MaterialReactTableList.jsx";
import useInterval from "../../Hooks/useInterval.jsx"
import PrintError from "../../Errors/Error.jsx";


const ListAccessoriesCategory = () => {
    const [categories, setCategories] = useState()
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const [delay, setDelay] = useState(100)

    useInterval(() => {
        async function getData() {
            try {
                 await AxiosInstanse.get(`consumables/accessories_category/`).then((res) => {
                    setCategories(res.data)
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
            accessorKey: 'name',
            header: 'Категория',
        },
        {
            accessorKey: 'slug',
            header: 'Ссылка',
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
                        data={categories}
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

export default ListAccessoriesCategory