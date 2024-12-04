# ***App Consumables***

## App
:::src.consumables.apps.ConsumablesConfig

## Admin

### Consumables
:::src.consumables.admin.ConsumablesAdmin

### Consumables categories
:::src.consumables.admin.CategoriesAdmin

### Accessories
:::src.consumables.admin.AccessoriesAdmin

### Accessories categories
:::src.consumables.admin.AccCatAdmin

## urls

### Home page

1. ```/```

### Consumables

1. ```consumables/```
2. ```consumables/search```
3. ```consumables/category/<slug:category_slug>```
4. ```consumables/(?P<pk>[-\w]+)$```
5. ```consumables/create/$```
6. ```consumables/(?P<pk>[-\w]+)/update$```
7. ```consumables/(?P<pk>[-\w]+)/delete$```
8. ```consumables/export/```
9. ```consumables/export/category/<slug:category_slug>```

### Accessories

1. ```accessories/```
2. ```accessories/search```
3. ```accessories/category/<slug:category_slug>```
4. ```accessories/(?P<pk>[-\w]+)$```
5. ```accessories/create/$```
6. ```accessories/(?P<pk>[-\w]+)/update$```
7. ```accessories/(?P<pk>[-\w]+)/delete$```
8. ```accessories/export/```
9. ```accessories/export/category/<slug:category_slug>```

### REST API

1. ```api/v1/consumable/```
2. ```api/v1/consumable_category/```
3. ```api/v1/accessories/```
4. ```api/v1/accessories_category```
