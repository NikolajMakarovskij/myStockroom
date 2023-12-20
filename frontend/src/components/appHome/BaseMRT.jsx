import * as React from "react";
import {MRT_Localization_RU} from "material-react-table/locales/ru";
import {Add as AddIcon, Delete as DeleteIcon, Edit as EditIcon} from "@mui/icons-material";
import {IconButton, MenuItem, Box} from "@mui/material";
import {Link} from "react-router-dom";
import {MaterialReactTable} from "material-react-table";


function BaseMRT(columns, data) {
    return(
        <Box>
            <MaterialReactTable
                columns={columns}
                data={data}
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
        </Box>
    )
}

export default BaseMRT