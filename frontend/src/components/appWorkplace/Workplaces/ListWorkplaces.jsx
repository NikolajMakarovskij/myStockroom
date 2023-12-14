import * as React from 'react';
import PropTypes from 'prop-types';
import {Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper,  tableCellClasses, styled, useTheme,
        Box, TablePagination, IconButton, createTheme, ThemeProvider, Menu, MenuItem,
    } from '@mui/material';
import FirstPageIcon from '@mui/icons-material/FirstPage';
import LastPageIcon from '@mui/icons-material/LastPage';
import {KeyboardArrowLeft, KeyboardArrowRight, } from '@mui/icons-material';
import ModalWorkplace from "./ModalWorkplace";
import RemoveWorkplace from "./RemoveWorkplace";
import { ruRU } from '@mui/material/locale';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import MenuWorkplace from "./MenuWorkplace";


const theme = createTheme(
  {
    palette: {
      primary: { main: '#1976d2' },
    },

  },
  ruRU,
);
//Table styles
const StyledTableCell = styled(TableCell)(({ theme }) => ({
      [`&.${tableCellClasses.head}`]: {
          backgroundColor: theme.palette.common.black,
          color: theme.palette.common.white,

      },
      [`&.${tableCellClasses.body}`]: {
            fontSize: 14,
      },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
        border: 0,
    },
}));


//Table pagination
function TablePaginationActions(props) {
  const theme = useTheme();
  const { count, page, rowsPerPage, onPageChange } = props;

  const handleFirstPageButtonClick = (event) => {
    onPageChange(event, 0);
  };

  const handleBackButtonClick = (event) => {
    onPageChange(event, page - 1);
  };

  const handleNextButtonClick = (event) => {
    onPageChange(event, page + 1);
  };

  const handleLastPageButtonClick = (event) => {
    onPageChange(event, Math.max(0, Math.ceil(count / rowsPerPage) - 1));
  };

  return (
    <Box sx={{ flexShrink: 0, ml: 2.5 }}>
      <IconButton
        onClick={handleFirstPageButtonClick}
        disabled={page === 0}
        aria-label="Первая страница"
      >
        {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
      </IconButton>
      <IconButton
        onClick={handleBackButtonClick}
        disabled={page === 0}
        aria-label="Предыдущая страница"
      >
        {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
      </IconButton>
      <IconButton
        onClick={handleNextButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="Следующая страница"
      >
        {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
      </IconButton>
      <IconButton
        onClick={handleLastPageButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="Последняя страница"
      >
        {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
      </IconButton>
    </Box>
  );
}

TablePaginationActions.propTypes = {
      count: PropTypes.number.isRequired,
      onPageChange: PropTypes.func.isRequired,
      page: PropTypes.number.isRequired,
      rowsPerPage: PropTypes.number.isRequired,
};



const ListWorkplace = (props) => {
    const {workplaces} = props
    const [page, setPage] = React.useState(0);
    const [rowsPerPage, setRowsPerPage] = React.useState(100);

    // Avoid a layout jump when reaching the last page with empty rows.
    const emptyRows =
        page > 0 ? Math.max(0, (1 + page) * rowsPerPage - workplaces.length) : 0;

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };
    const [anchorElMenu, setAnchorElMenu] = React.useState(null);
    const openMenu = Boolean(anchorElMenu);
    const handleClickMenu = (event) => {
        setAnchorElMenu(event.currentTarget);
    };
    const handleCloseMenu = () => {
        setAnchorElMenu(null);
    };

    return (
        <Paper sx={{ overflow: 'hidden' }}>
            <TableContainer  >
                <Table stickyHeader aria-label="sticky table">
                    <TableHead align="center" >
                        <ThemeProvider theme={theme}>
                            <TableRow>
                                <TablePagination
                                    rowsPerPageOptions={[10, 25, 100, { label: 'Все', value: -1 }]}
                                    colSpan={3}
                                    count={workplaces.length}
                                    rowsPerPage={rowsPerPage}
                                    page={page}
                                    SelectProps={{
                                        inputProps: {
                                          'aria-label': 'rows per page',
                                        },
                                        native: true,
                                    }}
                                  onPageChange={handleChangePage}
                                  onRowsPerPageChange={handleChangeRowsPerPage}
                                  ActionsComponent={TablePaginationActions}
                                />
                            </TableRow>
                        </ThemeProvider>
                        <StyledTableRow >
                            <StyledTableCell align="center">№ П/П</StyledTableCell>
                            <StyledTableCell align="center">Рабочие места</StyledTableCell>
                            <StyledTableCell align="center">Кабинет</StyledTableCell>
                            <StyledTableCell align="center">Этаж</StyledTableCell>
                            <StyledTableCell align="center">Здание</StyledTableCell>
                            <StyledTableCell align="center"></StyledTableCell>
                            <StyledTableCell align="center"></StyledTableCell>
                            <StyledTableCell align="center"></StyledTableCell>
                        </StyledTableRow>
                    </TableHead>
                    <TableBody>
                    {!workplaces || workplaces.length === 0 ? (
                        <TableRow >
                            <TableCell colSpan="6" align="center">
                                <b>Пока ничего нет</b>
                            </TableCell>
                        </TableRow>
                    ) : (rowsPerPage > 0
                        ? workplaces.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                        : workplaces
                        ).map((results, index) => (
                            <TableRow hover>
                                <TableCell align="center">
                                    <IconButton
                                        aria-label="more"
                                        id="long-button"
                                        aria-controls={openMenu ? 'long-menu' : undefined}
                                        aria-expanded={openMenu ? 'true' : undefined}
                                        aria-haspopup="true"
                                        onClick={handleClickMenu}
                                    >
                                        <MoreVertIcon />
                                    </IconButton>
                                    <Menu
                                        id="long-menu"
                                        MenuListProps={{
                                            'aria-labelledby': 'long-button',
                                        }}
                                        anchorEl={anchorElMenu}
                                        open={openMenu}
                                        onClose={handleCloseMenu}
                                    >
                                        <MenuItem onClick={handleCloseMenu}>
                                            <ModalWorkplace
                                                create={true}
                                                resetState={props.resetState}
                                                newWorkplace={true}
                                            />
                                        </MenuItem>
                                        <MenuItem onClick={handleCloseMenu}>
                                            <ModalWorkplace
                                                create={false}
                                                workplace={workplaces}
                                                resetState={props.resetState}
                                                newWorkplace={props.newWorkplace}
                                            />
                                        </MenuItem>
                                        <MenuItem onClick={handleCloseMenu}>
                                            <RemoveWorkplace
                                                id={results.id}
                                                resetState={props.resetState}
                                            />
                                        </MenuItem>
                                    </Menu>
                                    {index + 1}
                                </TableCell>
                                <TableCell align="center">{results.name}</TableCell>
                                <TableCell align="center">{results.room.name}</TableCell>
                                <TableCell align="center">{results.room.floor}</TableCell>
                                <TableCell align="center">{results.room.building}</TableCell>
                                <TableCell align="center">
                                            <ModalWorkplace
                                                create={true}
                                                resetState={props.resetState}
                                                newWorkplace={true}
                                            />
                                </TableCell>
                                <TableCell>
                                            <ModalWorkplace
                                                create={false}
                                                workplaces={workplaces}
                                                resetState={props.resetState}
                                                newWorkplace={props.newWorkplace}
                                            />
                                </TableCell>
                                <TableCell>
                                            <RemoveWorkplace
                                                id={results.id}
                                                resetState={props.resetState}
                                            />
                                </TableCell>
                            </TableRow>
                        )
                    )}
                    </TableBody>
                </Table>
            </TableContainer>
        </Paper>
    )
}

export default ListWorkplace