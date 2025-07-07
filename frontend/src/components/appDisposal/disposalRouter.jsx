import { React } from 'react'
import ListDisposal from '../appDisposal/ListDisposal'
import RemoveFromDisposal from '../appDisposal/RemoveFromDisposal'
import ListHistoryDisposal from '../appDisposal/ListHistoryDisposal'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const disposalRouter = [
  {
    path: '/disposal/list',
    element: [<NavBar key='disposal_list' drawerWidth={customWidth} content={<ListDisposal />} />],
  },
  {
    path: '/disposal/list/remove_from_disposal/:stock_model',
    element: [<NavBar key='remove_from_disposal' drawerWidth={customWidth} content={<RemoveFromDisposal />} />],
  },
  {
    path: '/history/disposal/list',
    element: [<NavBar key='history_disp_list' drawerWidth={customWidth} content={<ListHistoryDisposal />} />],
  },
]

export default disposalRouter
