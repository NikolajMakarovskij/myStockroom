import * as React from 'react'
import GridCards from '../Surface/GridCards'

const ConsumablesContent = [
  {
    key: 'consumables',
    title: 'Расходники',
    url_path: '/consumables/list',
    url_name: 'ListConsumables',
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'consumables_groups',
    title: 'Группы расходников',
    url_path: '/consumables/categories/list',
    url_name: 'ListConsumablesCategory',
    image: 'http://localhost/static/images/groups.svg',
  },
  {
    key: 'accessories',
    title: 'Комплектующие',
    url_path: '/accessories/list',
    url_name: 'ListAccessories',
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'accessories_groups',
    title: 'Группы комплектующих',
    url_path: '/accessories/categories/list',
    url_name: 'ListAccessoriesCategory',
    image: 'http://localhost/static/images/groups.svg',
  },
]
export { ConsumablesContent }

const IndexConsumables = () => {
  return <GridCards content={ConsumablesContent} />
}

export default IndexConsumables
