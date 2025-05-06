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
import NavBar from '../appHome/NavBar'

const customWidth = 200
const employeeRouter = [
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
]

export default employeeRouter
