import {
    MaterialReactTable,
} from 'material-react-table';
import {MRT_Localization_RU} from 'material-react-table/locales/ru';

export default function MaterialReactTableList ({columns, data, ...props}) {

    return(
        <>
            <MaterialReactTable
                {...props}
                columns={columns}
                data={data}
                muiTableBodyProps={{align: 'center'}}
                muiTableFooterProps={{align: 'center'}}
                muiTableHeadCellProps={{align: 'center'}}
                muiTableBodyCellProps={{align: 'center'}}
                localization={MRT_Localization_RU}
                enableColumnResizing={true}
                positionPagination='bottom'
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