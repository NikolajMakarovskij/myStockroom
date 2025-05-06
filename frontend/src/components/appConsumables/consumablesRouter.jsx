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
import NavBar from '../appHome/NavBar'

const customWidth = 200
const consumablesRouter = [
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
]

export default consumablesRouter
