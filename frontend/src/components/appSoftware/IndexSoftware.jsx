import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const SofwareContent = [
  {
    key: 'software',
    title: 'ОС',
    url_path: '/software/list',
    url_name: 'ListSofware',
    image: `http://${baseUrl}/static/images/software.svg`,
  },
  { key: 'os', title: 'ПО', url_path: '/os/list', url_name: 'ListOS', image: `http://${baseUrl}/static/images/os.svg` },
]
export { SofwareContent }

export default function IndexSoftware() {
  return <GridCards content={SofwareContent} />
}
