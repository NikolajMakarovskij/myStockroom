# ***App Accounting***

## App
:::src.accounting.apps.AccountingConfig

## Admin

### Accounting
:::src.accounting.admin.AccountingAdmin

### Categories
:::src.accounting.admin.CategoriesAdmin

## urls

### home

1. ```/```

### accounting

2. ```accounting/```
3. ```accounting/search```
4. ```accounting/category/<slug:category_slug>```
5. ```accounting/(?P<pk>[-\w]+)$```
6. ```accounting/create/$```
7. ```accounting/(?P<pk>[-\w]+)/update$```
8. ```accounting/(?P<pk>[-\w]+)/delete$```

### categories

1. ```categories/```
2. ```categories/search```
3. ```categories/create/$```
4. ```categories/(?P<pk>[-\w]+)/update$```
5. ```categories/(?P<pk>[-\w]+)/delete$```

### REST API

1. ```api/v1/accounting```
2. ```api/v1/accounting_category```
