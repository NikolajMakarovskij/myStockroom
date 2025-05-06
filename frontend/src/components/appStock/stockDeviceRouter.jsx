import { React } from 'react'
import ListStockDevices from '../appStock/Devices/ListStockDevices'
import ListHistoryDevice from '../appStock/Devices/ListHistoryDevice'
import RemoveFromStockDevice from '../appStock/Devices/RemoveFromStockDevice'
import AddToDecommission from '../appStock/Devices/AddToDecommission'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const stockDeviceRouter = [
  {
    path: '/stock/device/list',
    element: [<NavBar key='stock_dev_list' drawerWidth={customWidth} content={<ListStockDevices />} />],
  },
  {
    path: '/stock/device/list/:slug',
    element: [<NavBar key='stock_dev_groups' drawerWidth={customWidth} content={<ListStockDevices />} />],
  },
  {
    path: '/stock/device/list/remove_from_stock/:stock_model',
    element: [<NavBar key='remove_device_from_stock' drawerWidth={customWidth} content={<RemoveFromStockDevice />} />],
  },
  {
    path: '/stock/device/list/add_to_decommission/:stock_model',
    element: [<NavBar key='add_to_decommission' drawerWidth={customWidth} content={<AddToDecommission />} />],
  },
  {
    path: '/history/device/list',
    element: [<NavBar key='history_dev_list' drawerWidth={customWidth} content={<ListHistoryDevice />} />],
  },
  {
    path: '/history/device/list/:slug',
    element: [<NavBar key='history_dev_groups' drawerWidth={customWidth} content={<ListHistoryDevice />} />],
  },
]

export default stockDeviceRouter
