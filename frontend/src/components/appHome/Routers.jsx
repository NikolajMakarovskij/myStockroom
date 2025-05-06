import React from 'react'
import { createBrowserRouter } from 'react-router-dom'
import Home from './Home'
import NavBar from './NavBar'
import IndexWorkplace from '../appWorkplace/IndexWorkplace'
import ListWorkplace from '../appWorkplace/Workplaces/ListWorkplace'
import CreateWorkplace from '../appWorkplace/Workplaces/CreateWorkplace'
import UpdateWorkplace from '../appWorkplace/Workplaces/UpdateWorkplace'
import RemoveWorkplace from '../appWorkplace/Workplaces/RemoveWorkplace'
import ListRoom from '../appWorkplace/Rooms/ListRoom'
import CreateRoom from '../appWorkplace/Rooms/CreateRoom'
import UpdateRoom from '../appWorkplace/Rooms/UpdateRoom'
import RemoveRoom from '../appWorkplace/Rooms/RemoveRoom'
import IndexEmployee from '../appEmployee/IndexEmployee'
import ListDepartament from '../appEmployee/Departament/ListDepartament'
import CreateDepartament from '../appEmployee/Departament/CreateDepartament'
import RemoveDepartament from '../appEmployee/Departament/RemoveDepartament'
import UpdateDepartament from '../appEmployee/Departament/UpdateDepartament'
import ListPost from '../appEmployee/Post/ListPost'
import CreatePost from '../appEmployee/Post/CreatePost'
import RemovePost from '../appEmployee/Post/RemovePost'
import UpdatePost from '../appEmployee/Post/UpdatePost'
import ListEmployee from '../appEmployee/Employee/ListEmployee'
import CreateEmployee from '../appEmployee/Employee/CreateEmployee'
import UpdateEmployee from '../appEmployee/Employee/UpdateEmployee'
import RemoveEmployee from '../appEmployee/Employee/RemoveEmployee'
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
import IndexStock from '../appStock/IndexStock'
import ListStockConsumables from '../appStock/Consumables/ListStockConsumables'
import ListHistoryConsumables from '../appStock/Consumables/ListHistoryConsumables'
import ListConsumptionConsumables from '../appStock/Consumables/ListConsumptionConsumables'
import RemoveFromStockConsumable from '../appStock/Consumables/RemoveFromStockConsumable'
import ListStockAccessories from '../appStock/Accessories/ListStockAccessories'
import ListHistoryAccessories from '../appStock/Accessories/ListHistoryAccessories'
import ListConsumptionAccessories from '../appStock/Accessories/ListConsumptionAccessories'
import RemoveFromStockAccessories from '../appStock/Accessories/RemoveFromStockAccessories'
import ListStockDevices from '../appStock/Devices/ListStockDevices'
import ListHistoryDevice from '../appStock/Devices/ListHistoryDevice'
import RemoveFromStockDevice from '../appStock/Devices/RemoveFromStockDevice'
import AddHistoryToDevice from '../appDevice/Device/AddHistoryToDevice'
import IndexCounterparty from '../appCounterparty/IndexCounterparty'
import ListManufacturer from '../appCounterparty/appManufacturer/ListManufacturer'
import CreateManufacturer from '../appCounterparty/appManufacturer/CreateManufacturer'
import RemoveManufacturer from '../appCounterparty/appManufacturer/RemoveManufacturer'
import UpdateManufacturer from '../appCounterparty/appManufacturer/UpdateManufacturer'
import IndexConsumables from '../appConsumables/IndexConsumables'
import ListConsumables from '../appConsumables/Consumables/ListConsumables'
import CreateConsumable from '../appConsumables/Consumables/CreateConsumable'
import UpdateConsumable from '../appConsumables/Consumables/UpdateConsumable'
import RemoveConsumables from '../appConsumables/Consumables/RemoveConsumables'
import AddToStockConsumable from '../appConsumables/Consumables/AdToStockConsumable'
import ListConsumablesCategory from '../appConsumables/ConsumablesCategories/ListConsumablesCategory'
import CreateConsumableCategory from '../appConsumables/ConsumablesCategories/CreateConsumableCategory'
import UpdateConsumableCategory from '../appConsumables/ConsumablesCategories/UpdateConsumableCategory'
import RemoveConsumableCategory from '../appConsumables/ConsumablesCategories/RemoveConsumableCategory'
import ListAccessories from '../appConsumables/Accessories/ListAccessories'
import CreateAccessories from '../appConsumables/Accessories/CreateAccessories'
import UpdateAccessories from '../appConsumables/Accessories/UpdateAccessories'
import RemoveAccessories from '../appConsumables/Accessories/RemoveAccessories'
import AddToStockAccessories from '../appConsumables/Accessories/AdToStockAccessories'
import ListAccessoriesCategory from '../appConsumables/AccessoriesCategories/ListAccessoriesCategory'
import CreateAccessoriesCategory from '../appConsumables/AccessoriesCategories/CreateAccessoriesCategory'
import UpdateAccessoriesCategory from '../appConsumables/AccessoriesCategories/UpdateAccessoriesCategory'
import RemoveAccessoriesCategory from '../appConsumables/AccessoriesCategories/RemoveAccessoriesCategory'
import IndexAccounting from '../appAccounting/IndexAccounting'
import ListAccounting from '../appAccounting/Accounting/ListAccounting'
import CreateAccounting from '../appAccounting/Accounting/CreateAccounting'
import UpdateAccounting from '../appAccounting/Accounting/UpdateAccounting'
import RemoveAccounting from '../appAccounting/Accounting/RemoveAccounting'
import ListAccountingCategory from '../appAccounting/AccountingCategories/ListAccountingCategory'
import CreateAccountingCategory from '../appAccounting/AccountingCategories/CreateAccountingCategory'
import UpdateAccountingCategory from '../appAccounting/AccountingCategories/UpdateAccountingCategory'
import RemoveAccountingCategory from '../appAccounting/AccountingCategories/RemoveAccountingCategory'
import IndexSignature from '../appSignature/IndexSignature'
import IndexSoftware from '../appSoftware/IndexSoftware'
import ListOS from '../appSoftware/OS/ListOS'
import ListSofware from '../appSoftware/Software/ListSofware'
import ListDecommission from '../appDecommission/ListDecommission'
import AddToDecommission from '../appStock/Devices/AddToDecommission'
import AddToDisposal from '../appDecommission/AddToDisposal'
import RemoveFromDecommission from '../appDecommission/RemoveFromDecommission'
import ListDisposal from '../appDisposal/ListDisposal'

import RemoveFromDisposal from '../appDisposal/RemoveFromDisposal'

const customWidth = 200
const Routers = createBrowserRouter([
  //Home
  { path: '/', element: [<NavBar key='home' drawerWidth={customWidth} content={<Home />} />] },
  //Workplace
  { path: '/workplace', element: [<NavBar key='workplace' drawerWidth={customWidth} content={<IndexWorkplace />} />] },
  {
    path: '/workplace/list',
    element: [<NavBar key='workplace_list' drawerWidth={customWidth} content={<ListWorkplace />} />],
  },
  {
    path: '/workplace/list/create',
    element: [<NavBar key='workplace_create' drawerWidth={customWidth} content={<CreateWorkplace />} />],
  },
  {
    path: '/workplace/list/edit/:id',
    element: [<NavBar key='workplace_edit' drawerWidth={customWidth} content={<UpdateWorkplace />} />],
  },
  {
    path: '/workplace/list/remove/:id',
    element: [<NavBar key='workplace_remove' drawerWidth={customWidth} content={<RemoveWorkplace />} />],
  },
  { path: '/room/list', element: [<NavBar key='room_list' drawerWidth={customWidth} content={<ListRoom />} />] },
  {
    path: '/room/list/create',
    element: [<NavBar key='room_create' drawerWidth={customWidth} content={<CreateRoom />} />],
  },
  {
    path: '/room/list/edit/:id',
    element: [<NavBar key='room_edit' drawerWidth={customWidth} content={<UpdateRoom />} />],
  },
  {
    path: '/room/list/remove/:id',
    element: [<NavBar key='room_remove' drawerWidth={customWidth} content={<RemoveRoom />} />],
  },
  //Employee
  { path: '/employee', element: [<NavBar key='employee' drawerWidth={customWidth} content={<IndexEmployee />} />] },
  {
    path: '/employee/list',
    element: [<NavBar key='empl_list' drawerWidth={customWidth} content={<ListEmployee />} />],
  },
  {
    path: '/employee/list/create',
    element: [<NavBar key='empl_create' drawerWidth={customWidth} content={<CreateEmployee />} />],
  },
  {
    path: '/employee/list/edit/:id',
    element: [<NavBar key='empl_edit' drawerWidth={customWidth} content={<UpdateEmployee />} />],
  },
  {
    path: '/employee/list/remove/:id',
    element: [<NavBar key='empl_remove' drawerWidth={customWidth} content={<RemoveEmployee />} />],
  },
  {
    path: '/departament/list',
    element: [<NavBar key='dep_list' drawerWidth={customWidth} content={<ListDepartament />} />],
  },
  {
    path: '/departament/list/create',
    element: [<NavBar key='dep_create' drawerWidth={customWidth} content={<CreateDepartament />} />],
  },
  {
    path: '/departament/list/edit/:id',
    element: [<NavBar key='dep_edit' drawerWidth={customWidth} content={<UpdateDepartament />} />],
  },
  {
    path: '/departament/list/remove/:id',
    element: [<NavBar key='dep_remove' drawerWidth={customWidth} content={<RemoveDepartament />} />],
  },
  { path: '/post/list', element: [<NavBar key='post_list' drawerWidth={customWidth} content={<ListPost />} />] },
  {
    path: '/post/list/create',
    element: [<NavBar key='post_create' drawerWidth={customWidth} content={<CreatePost />} />],
  },
  {
    path: '/post/list/edit/:id',
    element: [<NavBar key='post_edit' drawerWidth={customWidth} content={<UpdatePost />} />],
  },
  {
    path: '/post/list/remove/:id',
    element: [<NavBar key='post_remove' drawerWidth={customWidth} content={<RemovePost />} />],
  },
  //Counterparty
  {
    path: '/counterparty',
    element: [<NavBar key='counterparty' drawerWidth={customWidth} content={<IndexCounterparty />} />],
  },
  {
    path: '/manufacturer/list',
    element: [<NavBar key='manufacturer_list' drawerWidth={customWidth} content={<ListManufacturer />} />],
  },
  {
    path: '/manufacturer/list/create',
    element: [<NavBar key='manufacturer_create' drawerWidth={customWidth} content={<CreateManufacturer />} />],
  },
  {
    path: '/manufacturer/list/edit/:id',
    element: [<NavBar key='manufacturer_edit' drawerWidth={customWidth} content={<UpdateManufacturer />} />],
  },
  {
    path: '/manufacturer/list/remove/:id',
    element: [<NavBar key='manufacturer_remove' drawerWidth={customWidth} content={<RemoveManufacturer />} />],
  },
  //Consumables
  {
    path: '/consumables',
    element: [<NavBar key='consumables' drawerWidth={customWidth} content={<IndexConsumables />} />],
  },
  {
    path: '/consumables/list',
    element: [<NavBar key='cons_list' drawerWidth={customWidth} content={<ListConsumables />} />],
  },
  {
    path: '/consumables/list/create',
    element: [<NavBar key='cons_create' drawerWidth={customWidth} content={<CreateConsumable />} />],
  },
  {
    path: '/consumables/list/edit/:id',
    element: [<NavBar key='cons_edit' drawerWidth={customWidth} content={<UpdateConsumable />} />],
  },
  {
    path: '/consumables/list/remove/:id',
    element: [<NavBar key='cons_remove' drawerWidth={customWidth} content={<RemoveConsumables />} />],
  },
  {
    path: '/consumables/list/add_to_stock/:id',
    element: [<NavBar key='cons_add_to_stock' drawerWidth={customWidth} content={<AddToStockConsumable />} />],
  },
  {
    path: '/consumables/categories/list',
    element: [<NavBar key='cons_cat_list' drawerWidth={customWidth} content={<ListConsumablesCategory />} />],
  },
  {
    path: '/consumables/categories/list/create',
    element: [<NavBar key='cons_cat_create' drawerWidth={customWidth} content={<CreateConsumableCategory />} />],
  },
  {
    path: '/consumables/categories/list/edit/:id',
    element: [<NavBar key='cons_cat_edit' drawerWidth={customWidth} content={<UpdateConsumableCategory />} />],
  },
  {
    path: '/consumables/categories/list/remove/:id',
    element: [<NavBar key='cons_cat_remove' drawerWidth={customWidth} content={<RemoveConsumableCategory />} />],
  },
  //Accessories
  {
    path: '/accessories/list',
    element: [<NavBar key='acc_list' drawerWidth={customWidth} content={<ListAccessories />} />],
  },
  {
    path: '/accessories/list/create',
    element: [<NavBar key='acc_create' drawerWidth={customWidth} content={<CreateAccessories />} />],
  },
  {
    path: '/accessories/list/edit/:id',
    element: [<NavBar key='acc_edit' drawerWidth={customWidth} content={<UpdateAccessories />} />],
  },
  {
    path: '/accessories/list/remove/:id',
    element: [<NavBar key='acc_remove' drawerWidth={customWidth} content={<RemoveAccessories />} />],
  },
  {
    path: '/accessories/list/add_to_stock/:id',
    element: [<NavBar key='acc_add_to_stock' drawerWidth={customWidth} content={<AddToStockAccessories />} />],
  },
  {
    path: '/accessories/categories/list',
    element: [<NavBar key='acc_cat_list' drawerWidth={customWidth} content={<ListAccessoriesCategory />} />],
  },
  {
    path: '/accessories/categories/list/create',
    element: [<NavBar key='acc_cat_create' drawerWidth={customWidth} content={<CreateAccessoriesCategory />} />],
  },
  {
    path: '/accessories/categories/list/edit/:id',
    element: [<NavBar key='acc_cat_edit' drawerWidth={customWidth} content={<UpdateAccessoriesCategory />} />],
  },
  {
    path: '/accessories/categories/list/remove/:id',
    element: [<NavBar key='acc_cat_remove' drawerWidth={customWidth} content={<RemoveAccessoriesCategory />} />],
  },
  //Accounting
  {
    path: '/accounting',
    element: [<NavBar key='accaunting' drawerWidth={customWidth} content={<IndexAccounting />} />],
  },
  {
    path: '/accounting/list',
    element: [<NavBar key='account_list' drawerWidth={customWidth} content={<ListAccounting />} />],
  },
  {
    path: '/accounting/list/create',
    element: [<NavBar key='account_create' drawerWidth={customWidth} content={<CreateAccounting />} />],
  },
  {
    path: '/accounting/list/edit/:id',
    element: [<NavBar key='account_edit' drawerWidth={customWidth} content={<UpdateAccounting />} />],
  },
  {
    path: '/accounting/list/remove/:id',
    element: [<NavBar key='account_remove' drawerWidth={customWidth} content={<RemoveAccounting />} />],
  },
  {
    path: '/accounting/categories/list',
    element: [<NavBar key='account_cat_list' drawerWidth={customWidth} content={<ListAccountingCategory />} />],
  },
  {
    path: '/accounting/categories/list/create',
    element: [<NavBar key='account_cat_create' drawerWidth={customWidth} content={<CreateAccountingCategory />} />],
  },
  {
    path: '/accounting/categories/list/edit/:id',
    element: [<NavBar key='account_cat_edit' drawerWidth={customWidth} content={<UpdateAccountingCategory />} />],
  },
  {
    path: '/accounting/categories/list/remove/:id',
    element: [<NavBar key='account_cat_remove' drawerWidth={customWidth} content={<RemoveAccountingCategory />} />],
  },
  //Device
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
  //Stock
  { path: '/stock', element: [<NavBar key='stock_device' drawerWidth={customWidth} content={<IndexStock />} />] },
  // Stock Consumables
  {
    path: '/stock/consumables/list',
    element: [<NavBar key='stock_con_list' drawerWidth={customWidth} content={<ListStockConsumables />} />],
  },
  {
    path: '/stock/consumables/list/:slug',
    element: [<NavBar key='stock_con_groups' drawerWidth={customWidth} content={<ListStockConsumables />} />],
  },
  {
    path: '/stock/consumables/list/remove_from_stock/:stock_model',
    element: [
      <NavBar key='remove_consumable_from_stock' drawerWidth={customWidth} content={<RemoveFromStockConsumable />} />,
    ],
  },
  {
    path: '/history/consumables/list',
    element: [<NavBar key='stock_history_con_list' drawerWidth={customWidth} content={<ListHistoryConsumables />} />],
  },
  {
    path: '/history/consumables/list/:slug',
    element: [<NavBar key='stock_history_con_groups' drawerWidth={customWidth} content={<ListHistoryConsumables />} />],
  },
  {
    path: '/consumption/consumables/list',
    element: [
      <NavBar key='stock_consumption_con_list' drawerWidth={customWidth} content={<ListConsumptionConsumables />} />,
    ],
  },
  {
    path: '/consumption/consumables/list/:slug',
    element: [
      <NavBar key='stock_consumption_con_groups' drawerWidth={customWidth} content={<ListConsumptionConsumables />} />,
    ],
  },
  // Stock Accessories
  {
    path: '/stock/accessories/list',
    element: [<NavBar key='stock_acc_list' drawerWidth={customWidth} content={<ListStockAccessories />} />],
  },
  {
    path: '/stock/accessories/list/:slug',
    element: [<NavBar key='stock_acc_groups' drawerWidth={customWidth} content={<ListStockAccessories />} />],
  },
  {
    path: '/stock/accessories/list/remove_from_stock/:stock_model',
    element: [
      <NavBar key='remove_accessories_from_stock' drawerWidth={customWidth} content={<RemoveFromStockAccessories />} />,
    ],
  },
  {
    path: '/history/accessories/list',
    element: [<NavBar key='stock_history_acc_list' drawerWidth={customWidth} content={<ListHistoryAccessories />} />],
  },
  {
    path: '/history/accessories/list/:slug',
    element: [<NavBar key='stock_history_acc_groups' drawerWidth={customWidth} content={<ListHistoryAccessories />} />],
  },
  {
    path: '/consumption/accessories/list',
    element: [
      <NavBar key='stock_consumption_acc_list' drawerWidth={customWidth} content={<ListConsumptionAccessories />} />,
    ],
  },
  {
    path: '/consumption/accessories/list/:slug',
    element: [
      <NavBar key='stock_consumption_acc_groups' drawerWidth={customWidth} content={<ListConsumptionAccessories />} />,
    ],
  },
  // Stock device
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
  // Decommission
  {
    path: '/decommission/list',
    element: [<NavBar key='decommission_list' drawerWidth={customWidth} content={<ListDecommission />} />],
  },
  {
    path: '/decommission/list/remove_from_decommission/:stock_model',
    element: [<NavBar key='remove_from_decommission' drawerWidth={customWidth} content={<RemoveFromDecommission />} />],
  },
  {
    path: '/decommission/list/add_to_disposal/:stock_model',
    element: [<NavBar key='add_to_disposal' drawerWidth={customWidth} content={<AddToDisposal />} />],
  },
  // Disposal
  {
    path: '/disposal/list',
    element: [<NavBar key='disposal_list' drawerWidth={customWidth} content={<ListDisposal />} />],
  },
  {
    path: '/disposal/list/remove_from_disposal/:stock_model',
    element: [<NavBar key='remove_from_disposal' drawerWidth={customWidth} content={<RemoveFromDisposal />} />],
  },

  // Signature
  { path: '/signature', element: [<NavBar key='signature' drawerWidth={customWidth} content={<IndexSignature />} />] },
  // SOFT
  { path: '/software', element: [<NavBar key='software' drawerWidth={customWidth} content={<IndexSoftware />} />] },
  {
    path: '/software/list',
    element: [<NavBar key='sofware_list' drawerWidth={customWidth} content={<ListSofware />} />],
  },
  { path: '/os/list', element: [<NavBar key='os' drawerWidth={customWidth} content={<ListOS />} />] },
])

export { Routers }
