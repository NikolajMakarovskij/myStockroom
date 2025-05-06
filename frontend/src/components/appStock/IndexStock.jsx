import * as React from 'react'
import GridCards from '../Surface/GridCards.jsx'

const StockContent = [
  {
    key: 'consumables_stock',
    title: 'Расходники',
    url_path: '/stock/consumables/list',
    url_name: 'ListStockConsumables',
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'history_consumables_stock',
    title: 'История расходников',
    url_path: '/history/consumables/list',
    url_name: 'ListHistoryConsumables',
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'consumption_consumables_stock',
    title: 'Расход расходников',
    url_path: '/consumption/consumables/list',
    url_name: 'ListConsumptionConsumables',
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'accessories_stock',
    title: 'Комплектующие',
    url_path: '/stock/accessories/list',
    url_name: 'ListStockAccessories',
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'history_accessories_stock',
    title: 'История комплектующих',
    url_path: '/history/accessories/list',
    url_name: 'ListHistoryAccessories',
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'consumption_accessories_stock',
    title: 'Расход комплектующих',
    url_path: '/consumption/accessories/list',
    url_name: 'ListConsumptionAccessories',
    image: 'http://localhost/static/images/accessories.svg',
  },
  {
    key: 'devices_stock',
    title: 'Устройста',
    url_path: '/stock/device/list',
    url_name: 'ListStockDevices',
    image: 'http://localhost/static/images/device.svg',
  },
  {
    key: 'decommission',
    title: 'Списание',
    url_path: '/decommission/list',
    url_name: 'ListDecommission',
    image: 'http://localhost/static/images/decommission.svg',
  },
  {
    key: 'disposal',
    title: 'Утилизация',
    url_path: '/disposal/list',
    url_name: 'ListDisposal',
    image: 'http://localhost/static/images/disposal.svg',
  },
  {
    key: 'history_devices_stock',
    title: 'История устройств',
    url_path: '/history/device/list',
    url_name: 'ListHistoryDevice',
    image: 'http://localhost/static/images/device.svg',
  },
]
export { StockContent }

const IndexStock = () => {
  return <GridCards content={StockContent} />
}

export default IndexStock
