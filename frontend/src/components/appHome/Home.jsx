import * as React from 'react'
import GridCards from '../Surface/GridCards.jsx'

const HomeContent = [
  {
    key: 'stock',
    title: 'Склад',
    url_path: '/stock',
    url_name: 'IndexStock',
    image: 'http://localhost/static/images/warehouse.svg',
  },
  {
    key: 'consumables',
    title: 'Расходники',
    url_path: '/consumables',
    url_name: 'IndexConsumables',
    image: 'http://localhost/static/images/consumables.svg',
  },
  {
    key: 'counterparty',
    title: 'Контрагенты',
    url_path: '/counterparty',
    url_name: 'IndexCounterparty',
    image: 'http://localhost/static/images/post.svg',
  },
  {
    key: 'workplace',
    title: 'Рабочие места',
    url_path: '/workplace',
    url_name: 'IndexWorkplace',
    image: 'http://localhost/static/images/workplace.svg',
  },
  {
    key: 'device',
    title: 'Устройства',
    url_path: '/device',
    url_name: 'IndexDevice',
    image: 'http://localhost/static/images/device.svg',
  },
  {
    key: 'software',
    title: 'Софт',
    url_path: '/software',
    url_name: 'IndexSoftware',
    image: 'http://localhost/static/images/software.svg',
  },
  {
    key: 'signature',
    title: 'ЭЦП',
    url_path: '/signature',
    url_name: 'IndexSignature',
    image: 'http://localhost/static/images/signature.svg',
  },
  {
    key: 'employee',
    title: 'Сотрудники',
    url_path: '/employee',
    url_name: 'IndexEmployee',
    image: 'http://localhost/static/images/employee.svg',
  },
  {
    key: 'accounting',
    title: 'Баланс',
    url_path: '/accounting',
    url_name: 'IndexAccounting',
    image: 'http://localhost/static/images/accounting.svg',
  },
]

const Home = () => {
  return <GridCards content={HomeContent} />
}

export default Home
