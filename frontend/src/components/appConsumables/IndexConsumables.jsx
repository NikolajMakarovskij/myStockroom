import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const ConsumablesContent = [
  {
    key: 'consumables',
    title: 'Расходники',
    url_path: '/consumables/list',
    url_name: 'ListConsumables',
    image: `http://${baseUrl}/static/images/consumables.svg`,
  },
  {
    key: 'consumables_groups',
    title: 'Группы расходников',
    url_path: '/consumables/categories/list',
    url_name: 'ListConsumablesCategory',
    image: `http://${baseUrl}/static/images/groups.svg`,
  },
  {
    key: 'accessories',
    title: 'Комплектующие',
    url_path: '/accessories/list',
    url_name: 'ListAccessories',
    image: `http://${baseUrl}/static/images/accessories.svg`,
  },
  {
    key: 'accessories_groups',
    title: 'Группы комплектующих',
    url_path: '/accessories/categories/list',
    url_name: 'ListAccessoriesCategory',
    image: `http://${baseUrl}/static/images/groups.svg`,
  },
]
export { ConsumablesContent }

export default function IndexConsumables() {
  return <GridCards content={ConsumablesContent} />
}
