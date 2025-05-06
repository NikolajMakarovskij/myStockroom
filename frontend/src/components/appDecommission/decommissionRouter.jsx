import ListDecommission from './ListDecommission'
import AddToDisposal from './AddToDisposal'
import RemoveFromDecommission from './RemoveFromDecommission'
import ListHistoryDecommission from './ListHistoryDecommission'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const decommissionRouter = [
  {
    path: '/decommission/list',
    element: [<NavBar key='decommission_list' drawerWidth={customWidth} content={<ListDecommission />} />],
  },
  {
    path: '/history/decommission/list',
    element: [<NavBar key='history_decom_list' drawerWidth={customWidth} content={<ListHistoryDecommission />} />],
  },
  {
    path: '/decommission/list/remove_from_decommission/:stock_model',
    element: [<NavBar key='remove_from_decommission' drawerWidth={customWidth} content={<RemoveFromDecommission />} />],
  },
  {
    path: '/decommission/list/add_to_disposal/:stock_model',
    element: [<NavBar key='add_to_disposal' drawerWidth={customWidth} content={<AddToDisposal />} />],
  },
]

export default decommissionRouter
