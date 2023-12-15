import * as React from 'react';
import {Box, Drawer, AppBar, CssBaseline, Toolbar, List, ListItem, ListItemButton, ListItemText, Button, IconButton,
    createTheme, ThemeProvider
} from '@mui/material/';
import MenuIcon from '@mui/icons-material/Menu'
import Home from "./Home";
import IndexWorkplace from "../appWorkplace/IndexWorkplace";
import {Link, useLocation} from "react-router-dom";


const menu = [
    {'title': "Главная", 'url_name': Home, 'url_path': '/'},
    {'title': "Раб. места", 'url_name': IndexWorkplace, 'url_path': '/workplace'},
    {'title': "Устройства", 'url_name': 'device:device_list', 'url_path': '/device' },
    {'title': "Сотрудники", 'url_name': 'employee:employee_index', 'url_path': '/employee' },
    {'title': "Софт", 'url_name': 'software:software_index', 'url_path': '/software' },
    {'title': "ЭЦП", 'url_name': 'signature:signature_list', 'url_path': '/signature' },
    {'title': "Склад", 'url_name': 'stockroom:stock_index', 'url_path': '/stockroom' },
    {'title': "Расходники", 'url_name': 'consumables:consumables_list', 'url_path': '/consumables' },
    {'title': "Комплектующие", 'url_name': 'consumables:accessories_list', 'url_path': '/accessories' },
    {'title': "Контрагенты", 'url_name': 'counterparty:counterparty', 'url_path': '/counterparty' },
    {'title': "Баланс", 'url_name': 'accounting:accounting_index', 'url_path': '/accounting'},
];

const navItems = ['Склад', 'Админка', 'Пользователь или авторизация'];

const darkTheme = createTheme({
  palette: {
      mode: 'dark',
  },
});


export default function NavBar(props) {
    const {drawerWidth, content} = props
    const location = useLocation()
    const path = location.pathname

    const [open, setOpen] = React.useState(false);

    const changeOpenStatus = () => {
        setOpen(!open)
    };

    const customDrawer = (
        <div>
            <Toolbar />
            <Box sx={{ overflow: 'auto' }}>
                <List>
                    {menu.map((res, index) => (
                        <ListItem key={index} disablePadding>
                            <ListItemButton component={Link} to={res.url_path} selected={res.url_path === path}>
                                <ListItemText primary={res.title} />
                            </ListItemButton>
                        </ListItem>
                    ))}
                </List>
            </Box>
        </div>
    )

    return (
        <Box sx={{ display: 'flex' }}>
            <CssBaseline />
            <ThemeProvider theme={darkTheme}>
                <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1, maxHeight: '60px'}} >
                    <Toolbar >
                        <IconButton onClick={changeOpenStatus} sx={{mr:2,display:{sm:"none"}}}>
                            <MenuIcon/>
                        </IconButton>
                        <Box sx={{ overflow: 'auto' }}>
                            <List>
                                <ListItem disablePadding>
                                    <ListItemButton component={Link} to='/' selected={'/' === path}>
                                        <ListItemText primary={'Главная'} />
                                    </ListItemButton>
                                </ListItem>
                            </List>
                        </Box>
                        <Box sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}/>
                        <Box sx={{ display: { xs: 'none', sm: 'block' }}} position='left'>
                            {navItems.map((item, index) => (
                                <Button key={index} component={Link} to={item.url_path} selected={item.url_path === path}>
                                    {item}
                                </Button>
                            ))}
                        </Box>
                    </Toolbar>

                </AppBar>
            </ThemeProvider>
            <ThemeProvider theme={darkTheme}>
                <Drawer
                    variant="permanent"
                    sx={{
                        display: {xs:'none', sm:'block'},
                        width: drawerWidth,
                        flexShrink: 0,
                        [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
                    }}
                >
                    {customDrawer}
                </Drawer>
                <Drawer
                    variant="temporary"
                    open = {open}
                    onClose = {changeOpenStatus}
                    sx={{
                        display: {xs:'block', sm:'none'},
                        width: drawerWidth,
                        flexShrink: 0,
                        [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
                    }}
                >
                    {customDrawer}
                </Drawer>
            </ThemeProvider>
            <Box component="main" sx={{ flexGrow: 1, p: 3, marginTop: '-80px' }}>
                <Toolbar />
                {content}
            </Box>
    </Box>
  );
}