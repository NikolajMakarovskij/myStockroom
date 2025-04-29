import * as React from 'react'
import GridCards from '../Surface/GridCards'

const WorkplaceContent = [
  {
    key: 'workplace',
    title: 'Рабочие места',
    url_path: '/workplace/list',
    url_name: 'ListWorkplace',
    image: 'http://localhost/static/images/workplace.svg',
  },
  {
    key: 'room',
    title: 'Помещение',
    url_path: '/room/list',
    url_name: 'ListRoom',
    image: 'http://localhost/static/images/room.svg',
  },
]
export { WorkplaceContent }

const IndexWorkplace = () => {
  return <GridCards content={WorkplaceContent} />
}

export default IndexWorkplace
