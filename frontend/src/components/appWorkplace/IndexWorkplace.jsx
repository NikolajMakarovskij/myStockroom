import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const WorkplaceContent = [
  {
    key: 'workplace',
    title: 'Рабочие места',
    url_path: '/workplace/list',
    url_name: 'ListWorkplace',
    image: `http://${baseUrl}/static/images/workplace.svg`,
  },
  {
    key: 'room',
    title: 'Помещение',
    url_path: '/room/list',
    url_name: 'ListRoom',
    image: `http://${baseUrl}/static/images/room.svg`,
  },
]
export { WorkplaceContent }

export default function IndexWorkplace() {
  return <GridCards content={WorkplaceContent} />
}
