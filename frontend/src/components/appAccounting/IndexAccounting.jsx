import * as React from 'react'
import GridCards from '../Surface/GridCards'

const baseUrl = import.meta.env.VITE_BASE_URL
const AccountingContent = [
  {
    key: 'accounting',
    title: 'Баланс',
    url_path: '/accounting/list',
    url_name: 'ListAccounting',
    image: `http://${baseUrl}/static/images/accounting.svg`,
  },
  {
    key: 'accounting_groups',
    title: 'Категории',
    url_path: '/accounting/categories/list',
    url_name: 'ListAccountingCategory',
    image: `http://${baseUrl}/static/images/groups.svg`,
  },
]
export { AccountingContent }

export default function IndexAccounting() {
  return <GridCards content={AccountingContent} />
}
