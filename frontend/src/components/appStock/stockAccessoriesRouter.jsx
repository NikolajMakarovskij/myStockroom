import { React } from 'react'
import ListStockAccessories from '../appStock/Accessories/ListStockAccessories'
import ListHistoryAccessories from '../appStock/Accessories/ListHistoryAccessories'
import ListConsumptionAccessories from '../appStock/Accessories/ListConsumptionAccessories'
import RemoveFromStockAccessories from '../appStock/Accessories/RemoveFromStockAccessories'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const stockAccessoriesRouter = [
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
]

export default stockAccessoriesRouter
