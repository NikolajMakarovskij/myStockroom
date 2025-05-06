import IndexDevice from '../appDevice/IndexDevice'
import ListDevice from '../appDevice/Device/ListDevice'
import CreateDevice from '../appDevice/Device/CreateDevice'
import UpdateDevice from '../appDevice/Device/UpdateDevice'
import RemoveDevice from '../appDevice/Device/RemoveDevice'
import ListDeviceCategory from '../appDevice/DeviceCategories/ListDeviceCategory'
import CreateDeviceCategory from '../appDevice/DeviceCategories/CreateDeviceCategory'
import UpdateDeviceCategory from '../appDevice/DeviceCategories/UpdateDeviceCategory'
import RemoveDeviceCategory from '../appDevice/DeviceCategories/RemoveDeviceCategory'
import AddToDeviceConsumable from '../appDevice/Device/AddToDeviceConsumable'
import AddToDeviceAccessories from '../appDevice/Device/AddToDeviceAccessories'
import AddToStockDevice from '../appDevice/Device/AddToStockDevice'
import MoveDevice from '../appDevice/Device/MoveDevice'
import AddHistoryToDevice from '../appDevice/Device/AddHistoryToDevice'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const deviceRouter = [
  { path: '/device', element: [<NavBar key='device' drawerWidth={customWidth} content={<IndexDevice />} />] },
  {
    path: '/device/list',
    element: [<NavBar key='device_groups' drawerWidth={customWidth} content={<ListDevice />} />],
  },
  {
    path: '/device/list/create',
    element: [<NavBar key='device_create' drawerWidth={customWidth} content={<CreateDevice />} />],
  },
  {
    path: '/device/list/edit/:id',
    element: [<NavBar key='device_edit' drawerWidth={customWidth} content={<UpdateDevice />} />],
  },
  {
    path: '/device/list/remove/:id',
    element: [<NavBar key='device_remove' drawerWidth={customWidth} content={<RemoveDevice />} />],
  },
  {
    path: '/device/list/add_consumable/:id',
    element: [<NavBar key='add_consumable' drawerWidth={customWidth} content={<AddToDeviceConsumable />} />],
  },
  {
    path: '/device/list/add_accessories/:id',
    element: [<NavBar key='add_accessories' drawerWidth={customWidth} content={<AddToDeviceAccessories />} />],
  },
  {
    path: '/device/list/add_to_stock/:id',
    element: [<NavBar key='add_accessories' drawerWidth={customWidth} content={<AddToStockDevice />} />],
  },
  {
    path: '/device/list/move_device/:id',
    element: [<NavBar key='move_device' drawerWidth={customWidth} content={<MoveDevice />} />],
  },
  {
    path: '/device/list/add_device_history/:id',
    element: [<NavBar key='add_device_history' drawerWidth={customWidth} content={<AddHistoryToDevice />} />],
  },
  {
    path: '/device/categories/list',
    element: [<NavBar key='device_groups' drawerWidth={customWidth} content={<ListDeviceCategory />} />],
  },
  {
    path: '/device/categories/list/create',
    element: [<NavBar key='device_create' drawerWidth={customWidth} content={<CreateDeviceCategory />} />],
  },
  {
    path: '/device/categories/list/edit/:id',
    element: [<NavBar key='device_edit' drawerWidth={customWidth} content={<UpdateDeviceCategory />} />],
  },
  {
    path: '/device/categories/list/remove/:id',
    element: [<NavBar key='device_remove' drawerWidth={customWidth} content={<RemoveDeviceCategory />} />],
  },
]

export default deviceRouter
