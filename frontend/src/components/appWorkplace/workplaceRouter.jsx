import IndexWorkplace from './IndexWorkplace'
import ListWorkplace from './Workplaces/ListWorkplace'
import CreateWorkplace from './Workplaces/CreateWorkplace'
import UpdateWorkplace from './Workplaces/UpdateWorkplace'
import RemoveWorkplace from './Workplaces/RemoveWorkplace'
import ListRoom from './Rooms/ListRoom'
import CreateRoom from './Rooms/CreateRoom'
import UpdateRoom from './Rooms/UpdateRoom'
import RemoveRoom from './Rooms/RemoveRoom'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const workplaceRouter = [
  {
    path: '/workplace',
    element: [<NavBar key='workplace' drawerWidth={customWidth} content={<IndexWorkplace />} />],
  },
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
]

export default workplaceRouter
