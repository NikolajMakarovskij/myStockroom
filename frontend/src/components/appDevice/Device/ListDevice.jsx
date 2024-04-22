import {React, useEffect, useMemo, useState, useCallback} from 'react'
import AxiosInstanse from "../../Axios.jsx";
import {Link} from "react-router-dom";
import {
    IconButton,
    MenuItem,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
} from '@mui/material';
import {Add as AddIcon, Edit as EditIcon, Delete as DeleteIcon,} from '@mui/icons-material';
import LinearIndeterminate from "../../appHome/ProgressBar.jsx";
import MaterialReactTableTabsList from "../../Tables/MaterialReactTableTabsList.jsx";
import {TreeItem, TreeView} from "@mui/x-tree-view";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";


const ListDevice = () => {
    const [device, setDevices] = useState()
    const [category, setCategory] = useState('')
    const [loading, setLoading] = useState(true)

    const GetData = useCallback(async () => {
         await AxiosInstanse.get(`/device/device_list/`, {timeout: 1000*30}).then((res) => {
            setDevices(res.data)
        })
    await AxiosInstanse.get(`/device/device_cat/`).then((res) => {
            setCategory(res.data)
            setLoading(false)
        })
    })

    useEffect(() =>{
        GetData();
    },[])

    const columns = useMemo(() => [
        {
            accessorKey: 'accounting',
            header: '',
        },
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
        <>
            {loading ? <LinearIndeterminate/> :
                <MaterialReactTableTabsList
                    columns={columns}
                    data={device}
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
                    renderDetailPanel={({ row }) =>
                        row.original ? (
                            <TreeView sx={{width: '100%'}}
                                defaultCollapseIcon={<ExpandMoreIcon />}
                                defaultExpandIcon={<ChevronRightIcon />}
                            >
                            {(row.original.consumable.length==0) ? <></> :
                                <TreeItem nodeId="1" label="Расходники">
                                    <TableContainer component={Paper}>
                                        <Table>
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell >Название</TableCell>
                                                    <TableCell >Описание</TableCell>
                                                    <TableCell >Количество</TableCell>
                                                    <TableCell >Разность</TableCell>
                                                    <TableCell >Примечание</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                {row.original.consumable.map((item, index) => (
                                                    <TableRow key={index}>
                                                        <TableCell >{item.name}</TableCell>
                                                        <TableCell >{item.description}</TableCell>
                                                        <TableCell >{item.quantity}</TableCell>
                                                        <TableCell >{item.difference}</TableCell>
                                                        <TableCell >{item.note}</TableCell>
                                                    </TableRow>
                                                ))}
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                                </TreeItem>
                            }
                            {(row.original.accessories.length==0) ? <></> :
                                <TreeItem nodeId="2" label="Комплектующие">
                                    <TableContainer component={Paper}>
                                        <Table>
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell >Название</TableCell>
                                                    <TableCell >Описание</TableCell>
                                                    <TableCell >Количество</TableCell>
                                                    <TableCell >Разность</TableCell>
                                                    <TableCell >Примечание</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                {row.original.accessories.map((item, index) => (
                                                    <TableRow key={index}>
                                                        <TableCell >{item.name}</TableCell>
                                                        <TableCell >{item.description}</TableCell>
                                                        <TableCell >{item.quantity}</TableCell>
                                                        <TableCell >{item.difference}</TableCell>
                                                        <TableCell >{item.note}</TableCell>
                                                    </TableRow>
                                                ))}
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                                </TreeItem>
                            }
                            {/*<TreeItem nodeId="3" label="История использования">
                                    <TableContainer component={Paper}>
                                        <Table>
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell >Количество</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                <TableRow>
                                                    <TableCell>{row.original.id}</TableCell>
                                                </TableRow>
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                                </TreeItem>*/}
                            </TreeView>
                        ) : null
                    }
                />
            }
        </>
    )



};

export default ListDevice