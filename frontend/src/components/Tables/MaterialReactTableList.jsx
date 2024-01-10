import {
    MaterialReactTable,
} from 'material-react-table';
//import {createTheme} from "@mui/material/styles";
import {IconButton, MenuItem} from '@mui/material';
import {MRT_Localization_RU} from 'material-react-table/locales/ru';

export default function MaterialReactTableList ({columns, data, ...props}) {

    return(
        <>
            <MaterialReactTable
                {...props}
                columns={columns}
                data={data}
                localization={MRT_Localization_RU}
                enableColumnResizing={true}
                positionPagination='both'
                enableRowNumbers='true'
                enableRowVirtualization='true'
                enableRowActions
                initialState= {({pagination: { pageSize: (data.length), pageIndex: 0 }})}
                muiPaginationProps={({
                    rowsPerPageOptions: [25, 50, 100,  { label: 'Все', value: data.length}],
                    showFirstButton: true,
                    showLastButton: true,
                    shape: 'rounded',
                })}
            />
        </>
    )
};