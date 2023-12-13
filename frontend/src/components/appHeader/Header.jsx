import * as React from 'react';
import PropTypes from 'prop-types';
import {AppBar, Box, Button, CssBaseline, IconButton, Menu, MenuItem, Toolbar, Typography} from '@mui/material/';
import {Link,} from 'react-router-dom';
import MenuIcon from '@mui/icons-material/Menu';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Home from '../appHome/Home';
import IndexWorkplace from "../appWorkplace/IndexWorkplace";

const menu = [
    {'title': "Главная страница", 'url_name': Home, 'url_path': '/'},
    {'title': "Раб. места", 'url_name': IndexWorkplace, 'url_path': '/workplace'},
    //{'title': "Устройства", 'url_name': 'device:device_list', 'url_path': '/device' },
    //{'title': "Сотрудники", 'url_name': 'employee:employee_index', 'url_path': '/employee' },
    //{'title': "Софт", 'url_name': 'software:software_index', 'url_path': '/software' },
    //{'title': "ЭЦП", 'url_name': 'signature:signature_list', 'url_path': '/signature' },
    //{'title': "Склад", 'url_name': 'stockroom:stock_index', 'url_path': '/stockroom' },
    //{'title': "Расходники", 'url_name': 'consumables:consumables_list', 'url_path': '/consumables' },
    //{'title': "Комплектующие", 'url_name': 'consumables:accessories_list', 'url_path': '/accessories' },
    //{'title': "Контрагенты", 'url_name': 'counterparty:counterparty', 'url_path': '/counterparty' },
    //{'title': "Баланс", 'url_name': 'accounting:accounting_index', 'url_path': '/accounting'},
];


const navItems = ['Склад', 'Админка', 'Пользователь или авторизация'];

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function Header(props) {
  const [setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen((prevState) => !prevState);
  };

  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };



  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <ThemeProvider theme={darkTheme}>
      <AppBar>
        <Toolbar >
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            id="basic-button"
            aria-controls={open ? 'basic-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
            onClick={handleClick}
             sx={{ mr: 1, sm: 6 }}
          >
            <MenuIcon />
          </IconButton>
          <Menu
            id="basic-menu"
            anchorEl={anchorEl}
            open={open}
            onClose={handleClose}
            MenuListProps={{
              'aria-labelledby': 'basic-button',
            }}
          >
            {menu.map((item) => (
                <MenuItem key={item.url_path}>
                    <Link to={item.url_path} element={item.url_name}>{item.title}</Link>
                  </MenuItem>
                ))}
          </Menu>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: 'none' } }}
          >
            <MenuIcon />
          </IconButton>
          <Typography
            variant="h6"
            component="div"
            sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}
          >
              <Link to='/' element={Home}>Главная</Link>
          </Typography>
          <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
              {navItems.map((item) => (
                  <Button key={item}>
                    {item}
                  </Button>
                ))}
          </Box>
        </Toolbar>
      </AppBar>
      </ThemeProvider>
    </Box>
  );
}

Header.propTypes = {
  /**
   * Injected by the documentation to work in an iframe.
   * You won't need it on your project.
   */
  window: PropTypes.func,
};

export default Header;