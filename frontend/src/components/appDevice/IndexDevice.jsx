import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const DeviceContent = [
  {
    key: 'device_list',
    title: 'Устройства',
    url_path: '/device/list',
    url_name: 'ListDevice',
    image: `http://${baseUrl}/static/images/device.svg`,
  },
  {
    key: 'device_categories_list',
    title: 'Группы устройств',
    url_path: '/device/categories/list',
    url_name: 'ListDeviceCategory',
    image: `http://${baseUrl}/static/images/groups.svg`,
  },
]
export { DeviceContent }

export default function IndexDevice() {
  return <GridCards content={DeviceContent} />
}
