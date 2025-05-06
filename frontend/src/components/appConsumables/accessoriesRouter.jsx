import ListAccessories from '../appConsumables/Accessories/ListAccessories'
import CreateAccessories from '../appConsumables/Accessories/CreateAccessories'
import UpdateAccessories from '../appConsumables/Accessories/UpdateAccessories'
import RemoveAccessories from '../appConsumables/Accessories/RemoveAccessories'
import AddToStockAccessories from '../appConsumables/Accessories/AdToStockAccessories'
import ListAccessoriesCategory from '../appConsumables/AccessoriesCategories/ListAccessoriesCategory'
import CreateAccessoriesCategory from '../appConsumables/AccessoriesCategories/CreateAccessoriesCategory'
import UpdateAccessoriesCategory from '../appConsumables/AccessoriesCategories/UpdateAccessoriesCategory'
import RemoveAccessoriesCategory from '../appConsumables/AccessoriesCategories/RemoveAccessoriesCategory'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const accessoriesRouter = [
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
]

export default accessoriesRouter
