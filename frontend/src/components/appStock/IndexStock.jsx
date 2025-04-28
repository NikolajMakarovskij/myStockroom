import * as React from 'react'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import { Card, CardActionArea, CardContent, CardMedia, Grid, Typography } from '@mui/material'
import { Link } from 'react-router-dom'
import ListStockDevices from './Devices/ListStockDevices.jsx'
import ListStockConsumables from './Consumables/ListStockConsumables.jsx'
import ListHistoryConsumables from './Consumables/ListHistoryConsumables.jsx'
import ListConsumptionConsumables from './Consumables/ListConsumptionConsumables.jsx'
import ListStockAccessories from './Accessories/ListStockAccessories.jsx'
import ListHistoryAccessories from './Accessories/ListHistoryAccessories.jsx'
import ListConsumptionAccessories from './Accessories/ListConsumptionAccessories.jsx'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

const StockContent = [
  {
    key: 'consumables_stock',
    title: 'Расходники',
    url_path: '/stock/consumables/list',
    url_name: ListStockConsumables,
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'history_consumables_stock',
    title: 'История расходников',
    url_path: '/history/consumables/list',
    url_name: ListHistoryConsumables,
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'consumption_consumables_stock',
    title: 'Расход расходников',
    url_path: '/consumption/consumables/list',
    url_name: ListConsumptionConsumables,
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'accessories_stock',
    title: 'Комплектующие',
    url_path: '/stock/accessories/list',
    url_name: ListStockAccessories,
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'history_accessories_stock',
    title: 'История комплектующих',
    url_path: '/history/accessories/list',
    url_name: ListHistoryAccessories,
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'consumption_accessories_stock',
    title: 'Расход комплектующих',
    url_path: '/consumption/accessories/list',
    url_name: ListConsumptionAccessories,
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'devices_stock',
    title: 'Устройста',
    url_path: '/stock/device/list',
    url_name: ListStockDevices,
    image: 'http://localhost/static/images/device.svg',
  },
]
export { StockContent }

const IndexStock = () => {
  return (
    <Grid container style={{ marginLeft: '50px' }}>
      <ThemeProvider theme={darkTheme}>
        {StockContent.map((item) => (
          <Grid key={item.key} size={{ xs: 1, sm: 6, md: 4 }} style={{ marginBottom: '80px' }}>
            <Card
              sx={{ minWidth: 200, maxWidth: 200, minHeight: 200, maxHeight: 200, borderRadius: 5, display: 'flex' }}
            >
              <CardActionArea
                component={Link}
                to={item.url_path}
                element={item.url_name}
                sx={{ display: 'flex', flexDirection: 'column' }}
              >
                <CardContent>
                  <Typography gutterBottom component='div'>
                    {item.title}
                  </Typography>
                </CardContent>
                <CardMedia
                  sx={{ border: 0, minWidth: 120, maxWidth: 120, minHeight: 120, maxHeight: 120 }}
                  component='img'
                  image={item.image}
                  alt={item.title}
                />
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </ThemeProvider>
    </Grid>
  )
}

export default IndexStock
