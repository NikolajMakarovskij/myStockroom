import { React, useState } from 'react'
import PropTypes from 'prop-types'
import {
  Box,
  Drawer,
  AppBar,
  CssBaseline,
  Toolbar,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  Button,
  IconButton,
  createTheme,
  ThemeProvider,
} from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'
import { Link, useLocation } from 'react-router-dom'

import { WorkplaceContent } from '../appWorkplace/IndexWorkplace'
import { StockContent } from '../appStock/IndexStock'
import { EmployeeContent } from '../appEmployee/IndexEmployee'
import LoginApp from '../appAuth/LoginApp'
import useSession from '../appAuth/Hooks/useSession.jsx'
import useLogout from '../appAuth/Hooks/useLogout.jsx'

const menu = [
  { id: 'menu_item_1', title: 'Главная', url_path: '/', menu: [] },
  { id: 'menu_item_2', title: 'Раб. места', url_path: '/workplace', menu: WorkplaceContent },
  { id: 'menu_item_3', title: 'Устройства', url_path: '/device', menu: [] },
  { id: 'menu_item_4', title: 'Сотрудники', url_path: '/employee', menu: EmployeeContent },
  { id: 'menu_item_5', title: 'Софт', url_path: '/software', menu: [] },
  { id: 'menu_item_6', title: 'ЭЦП', url_path: '/signature', menu: [] },
  { id: 'menu_item_7', title: 'Склад', url_path: '/stock', menu: StockContent },
  { id: 'menu_item_8', title: 'Расходники', url_path: '/consumables/list', menu: [] },
  { id: 'menu_item_9', title: 'Комплектующие', url_path: '/accessories/list', menu: [] },
  { id: 'menu_item_10', title: 'Контрагенты', url_path: '/counterparty', menu: [] },
  { id: 'menu_item_11', title: 'Баланс', url_path: '/accounting', menu: [] },
]

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function NavBar(props) {
  const getSession = useSession()
  const getLogout = useLogout()
  const { drawerWidth, content } = props
  const location = useLocation()
  const path = location.pathname
  const [open, setOpen] = useState(false)

  const changeOpenStatus = () => {
    setOpen(!open)
  }

  const customDrawer = (
    <div>
      <Toolbar />
      <Box sx={{ overflow: 'auto' }}>
        <List>
          {menu.map((res) => (
            <ListItem key={res.id} disablePadding>
              <ListItemButton
                key={`button_${res.id}`}
                component={Link}
                to={res.url_path}
                selected={res.url_path === path}
              >
                <ListItemText primary={res.title} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </Box>
    </div>
  )
  return (
    <div>
      {!getSession.isAuthenticated ? (
        <LoginApp />
      ) : (
        <Box sx={{ display: 'flex' }}>
          <CssBaseline />
          <ThemeProvider theme={darkTheme}>
            <AppBar position='fixed' sx={{ zIndex: (theme) => theme.zIndex.drawer + 1, maxHeight: '60px' }}>
              <Toolbar>
                <IconButton onClick={changeOpenStatus} sx={{ mr: 2, display: { sm: 'none' } }}>
                  <MenuIcon />
                </IconButton>
                <Box sx={{ overflow: 'auto' }}>
                  <List>
                    <ListItem key='item_home' disablePadding>
                      <ListItemButton key='home' component={Link} to='/' selected={'/' === path}>
                        <ListItemText primary={'Главная'} />
                      </ListItemButton>
                    </ListItem>
                  </List>
                </Box>
                <Box sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }} />
                <Box sx={{ display: { xs: 'none', sm: 'block' } }} position='left'>
                  <Button key='username'>{getSession.username}</Button>
                  <Button key='logout' component={Link} to={`/`} onClick={getLogout}>
                    Выйти
                  </Button>
                </Box>
              </Toolbar>
            </AppBar>
          </ThemeProvider>
          <ThemeProvider theme={darkTheme}>
            <Drawer
              variant='permanent'
              sx={{
                display: { xs: 'none', sm: 'block' },
                width: drawerWidth,
                flexShrink: 0,
                [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
              }}
            >
              {customDrawer}
            </Drawer>
            <Drawer
              variant='temporary'
              open={open}
              onClose={changeOpenStatus}
              sx={{
                display: { xs: 'block', sm: 'none' },
                width: drawerWidth,
                flexShrink: 0,
                [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
              }}
            >
              {customDrawer}
            </Drawer>
          </ThemeProvider>
          <Box component='main' sx={{ flexGrow: 1, p: 3 }}>
            <Toolbar />
            {content}
          </Box>
        </Box>
      )}
    </div>
  )
}

NavBar.propTypes = {
  drawerWidth: PropTypes.number,
  content: PropTypes.object,
}
