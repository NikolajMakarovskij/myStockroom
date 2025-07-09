import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const CounterpartyContent = [
  {
    key: 'manufacturer',
    title: 'Производители',
    url_path: '/manufacturer/list',
    url_name: 'ListManufacturer',
    image: `http://${baseUrl}/static/images/manufacturer.svg`,
  },
]
export { CounterpartyContent }

export default function IndexCounterparty() {
  return <GridCards content={CounterpartyContent} />
}
