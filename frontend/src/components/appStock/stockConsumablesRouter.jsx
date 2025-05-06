import IndexStock from '../appStock/IndexStock'
import ListStockConsumables from '../appStock/Consumables/ListStockConsumables'
import ListHistoryConsumables from '../appStock/Consumables/ListHistoryConsumables'
import ListConsumptionConsumables from '../appStock/Consumables/ListConsumptionConsumables'
import RemoveFromStockConsumable from '../appStock/Consumables/RemoveFromStockConsumable'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const stockConsumablesRouter = [
  { path: '/stock', element: [<NavBar key='stock_device' drawerWidth={customWidth} content={<IndexStock />} />] },
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
]

export default stockConsumablesRouter
