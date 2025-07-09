import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const EmployeeContent = [
  {
    key: 'employee',
    title: 'Сотрудники',
    url_path: '/employee/list',
    url_name: 'ListEmployee',
    image: `http://${baseUrl}/static/images/employee.svg`,
  },
  {
    key: 'post',
    title: 'Должности',
    url_path: '/post/list',
    url_name: 'ListPost',
    image: `http://${baseUrl}/static/images/post.svg`,
  },
  {
    key: 'departament',
    title: 'Отделы',
    url_path: '/departament/list',
    url_name: 'ListDepartament',
    image: `http://${baseUrl}/static/images/departament.svg`,
  },
]
export { EmployeeContent }

export default function IndexEmployee() {
  return <GridCards content={EmployeeContent} />
}
