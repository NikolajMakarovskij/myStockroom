import * as React from 'react'
import GridCards from '../Surface/GridCards'

const CounterpartyContent = [
  {
    key: 'manufacturer',
    title: 'Производители',
    url_path: '/manufacturer/list',
    url_name: 'ListManufacturer',
    image: 'http://localhost/static/images/manufacturer.svg',
  },
]
export { CounterpartyContent }

export default function IndexCounterparty() {
  return <GridCards content={CounterpartyContent} />
}
