import { React } from 'react'
import IndexSoftware from '../appSoftware/IndexSoftware'
import ListOS from '../appSoftware/OS/ListOS'
import ListSofware from '../appSoftware/Software/ListSofware'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const softwareRouter = [
  { path: '/software', element: [<NavBar key='software' drawerWidth={customWidth} content={<IndexSoftware />} />] },
  {
    path: '/software/list',
    element: [<NavBar key='sofware_list' drawerWidth={customWidth} content={<ListSofware />} />],
  },
  { path: '/os/list', element: [<NavBar key='os' drawerWidth={customWidth} content={<ListOS />} />] },
]

export default softwareRouter
