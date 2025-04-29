import * as React from 'react'
import GridCards from '../Surface/GridCards'

const SofwareContent = [
  {
    key: 'software',
    title: 'ОС',
    url_path: '/software/list',
    url_name: 'ListSofware',
    image: 'http://localhost/static/images/software.svg',
  },
  { key: 'os', title: 'ПО', url_path: '/os/list', url_name: 'ListOS', image: 'http://localhost/static/images/os.svg' },
]
export { SofwareContent }

const IndexSoftware = () => {
  return <GridCards content={SofwareContent} />
}

export default IndexSoftware
