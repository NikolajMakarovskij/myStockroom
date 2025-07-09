import * as React from 'react'
import GridCards from '../Surface/GridCards.jsx'

const baseUrl = import.meta.env.VITE_BASE_URL
const HomeContent = [
  {
    key: 'stock',
    title: 'Склад',
    url_path: '/stock',
    url_name: 'IndexStock',
    image: `http://${baseUrl}/static/images/warehouse.svg`,
  },
  {
    key: 'consumables',
    title: 'Расходники',
    url_path: '/consumables',
    url_name: 'IndexConsumables',
    image: `http://${baseUrl}/static/images/consumables.svg`,
  },
  {
    key: 'counterparty',
    title: 'Контрагенты',
    url_path: '/counterparty',
    url_name: 'IndexCounterparty',
    image: `http://${baseUrl}/static/images/post.svg`,
  },
  {
    key: 'workplace',
    title: 'Рабочие места',
    url_path: '/workplace',
    url_name: 'IndexWorkplace',
    image: `http://${baseUrl}/static/images/workplace.svg`,
  },
  {
    key: 'device',
    title: 'Устройства',
    url_path: '/device',
    url_name: 'IndexDevice',
    image: `http://${baseUrl}/static/images/device.svg`,
  },
  {
    key: 'software',
    title: 'Софт',
    url_path: '/software',
    url_name: 'IndexSoftware',
    image: `http://${baseUrl}/static/images/software.svg`,
  },
  {
    key: 'signature',
    title: 'ЭЦП',
    url_path: '/signature',
    url_name: 'IndexSignature',
    image: `http://${baseUrl}/static/images/signature.svg`,
  },
  {
    key: 'employee',
    title: 'Сотрудники',
    url_path: '/employee',
    url_name: 'IndexEmployee',
    image: `http://${baseUrl}/static/images/employee.svg`,
  },
  {
    key: 'accounting',
    title: 'Баланс',
    url_path: '/accounting',
    url_name: 'IndexAccounting',
    image: `http://${baseUrl}/static/images/accounting.svg`,
  },
]

export default function Home() {
  return <GridCards content={HomeContent} baseUrl />
}
