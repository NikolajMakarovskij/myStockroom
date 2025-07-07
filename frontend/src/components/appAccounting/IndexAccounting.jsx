import * as React from 'react'
import GridCards from '../Surface/GridCards'

const AccountingContent = [
  {
    key: 'accounting',
    title: 'Баланс',
    url_path: '/accounting/list',
    url_name: 'ListAccounting',
    image: 'http://localhost/static/images/accounting.svg',
  },
  {
    key: 'accounting_groups',
    title: 'Категории',
    url_path: '/accounting/categories/list',
    url_name: 'ListAccountingCategory',
    image: 'http://localhost/static/images/groups.svg',
  },
]
export { AccountingContent }

export default function IndexAccounting() {
  return <GridCards content={AccountingContent} />
}
