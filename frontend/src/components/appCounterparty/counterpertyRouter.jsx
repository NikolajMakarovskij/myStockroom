import { React } from 'react'
import IndexCounterparty from './IndexCounterparty'
import ListManufacturer from './appManufacturer/ListManufacturer'
import CreateManufacturer from './appManufacturer/CreateManufacturer'
import RemoveManufacturer from './appManufacturer/RemoveManufacturer'
import UpdateManufacturer from './appManufacturer/UpdateManufacturer'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const counterpertyRouter = [
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
]

export default counterpertyRouter
