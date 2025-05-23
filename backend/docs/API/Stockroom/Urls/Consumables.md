# ***Consumables***

## REST API

### Stockroom

1. ```api/stockroom/stock_con_list/```
2. ```api/stockroom/stock_con_cat_list/```

### Methods

1. ```api/stockroom/add_to_stock_consumable/```
2. ```api/stockroom/add_to_device_consumable/```
3. ```api/stockroom/remove_from_stock_consumable/```

### Export

1. ```api/stockroom/export/```
2. ```api/stockroom/export/category/<slug:category_slug>```
3. ```api/stockroom/history/export/```
4. ```api/stockroom/history/export/category/<slug:category_slug>```

### History

1. ```api/stockroom/history_con_list/```
2. ```api/stockroom/consumption_con_list/```
3. ```api/stockroom/history_con_list/filter/(?P<stock_model_id>.+)/$```
4. ```api/stockroom/history_con_list/device/filter/(?P<deviceId>.+)/$```
