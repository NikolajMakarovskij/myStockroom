import { React } from 'react'
import IndexAccounting from '../appAccounting/IndexAccounting'
import ListAccounting from '../appAccounting/Accounting/ListAccounting'
import CreateAccounting from '../appAccounting/Accounting/CreateAccounting'
import UpdateAccounting from '../appAccounting/Accounting/UpdateAccounting'
import RemoveAccounting from '../appAccounting/Accounting/RemoveAccounting'
import ListAccountingCategory from '../appAccounting/AccountingCategories/ListAccountingCategory'
import CreateAccountingCategory from '../appAccounting/AccountingCategories/CreateAccountingCategory'
import UpdateAccountingCategory from '../appAccounting/AccountingCategories/UpdateAccountingCategory'
import RemoveAccountingCategory from '../appAccounting/AccountingCategories/RemoveAccountingCategory'
import NavBar from '../appHome/NavBar'

const customWidth = 200
const accountingRouter = [
  {
    path: '/accounting',
    element: [<NavBar key='accaunting' drawerWidth={customWidth} content={<IndexAccounting />} />],
  },
  {
    path: '/accounting/list',
    element: [<NavBar key='account_list' drawerWidth={customWidth} content={<ListAccounting />} />],
  },
  {
    path: '/accounting/list/create',
    element: [<NavBar key='account_create' drawerWidth={customWidth} content={<CreateAccounting />} />],
  },
  {
    path: '/accounting/list/edit/:id',
    element: [<NavBar key='account_edit' drawerWidth={customWidth} content={<UpdateAccounting />} />],
  },
  {
    path: '/accounting/list/remove/:id',
    element: [<NavBar key='account_remove' drawerWidth={customWidth} content={<RemoveAccounting />} />],
  },
  {
    path: '/accounting/categories/list',
    element: [<NavBar key='account_cat_list' drawerWidth={customWidth} content={<ListAccountingCategory />} />],
  },
  {
    path: '/accounting/categories/list/create',
    element: [<NavBar key='account_cat_create' drawerWidth={customWidth} content={<CreateAccountingCategory />} />],
  },
  {
    path: '/accounting/categories/list/edit/:id',
    element: [<NavBar key='account_cat_edit' drawerWidth={customWidth} content={<UpdateAccountingCategory />} />],
  },
  {
    path: '/accounting/categories/list/remove/:id',
    element: [<NavBar key='account_cat_remove' drawerWidth={customWidth} content={<RemoveAccountingCategory />} />],
  },
]

export default accountingRouter
