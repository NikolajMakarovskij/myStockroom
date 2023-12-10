import * as React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import {createTheme, ThemeProvider} from "@mui/material/styles";

const menu = [
    {'title': "Главная страница", 'url_name': 'core:index'},
    {'title': "Раб. места", 'url_name': 'workplace:workplace_index'},
    {'title': "Устройства", 'url_name': 'device:device_list'},
    {'title': "Сотрудники", 'url_name': 'employee:employee_index'},
    {'title': "Софт", 'url_name': 'software:software_index'},
    {'title': "ЭЦП", 'url_name': 'signature:signature_list'},
    {'title': "Склад", 'url_name': 'stockroom:stock_index'},
    {'title': "Расходники", 'url_name': 'consumables:consumables_list'},
    {'title': "Комплектующие", 'url_name': 'consumables:accessories_list'},
    {'title': "Контрагенты", 'url_name': 'counterparty:counterparty'},
    {'title': "Баланс", 'url_name': 'accounting:accounting_index'},
]

const drawerWidth = 240;
const navItems = ['Склад', 'Админка', 'Пользователь или авторизация'];

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function Header(props) {
  const { window } = props;
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen((prevState) => !prevState);
  };
  const drawer = (
    <Box onClick={handleDrawerToggle} sx={{ textAlign: 'center' }}>
      <Divider />
      <List>
        {navItems.map((item) => (
          <ListItem key={item} disablePadding>
            <ListItemButton sx={{ textAlign: 'center' }}>
              <ListItemText theme={item} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const container = window !== undefined ? () => window().document.body : undefined;

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
                  <MenuItem key={item.url_name}>
                    {item.title}
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
            Главная
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