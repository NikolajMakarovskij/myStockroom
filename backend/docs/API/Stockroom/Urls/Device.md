# ***Devices***

## REST API

### Stockroom

1. ```api/stockroom/stock_dev_list/```
2. ```api/stockroom/stock_dev_cat_list/```

### Methods

1. ```api/stockroom/add_to_stock_device/```
2. ```api/stockroom/remove_from_stock_device/```
3. ```api/stockroom/move_device/```
4. ```api/stockroom/add_device_history/```

### Export

1. ```api/stockroom/devices/export/```
2. ```api/stockroom/devices/export/category/<slug:category_slug>```

### History

1. ```api/stockroom/history_dev_list/```
2. ```api/stockroom/consumption_con_list/```
3. ```api/stockroom/history_dev_list/filter/(?P<stock_model_id>.+)/$```
4. ```api/stockroom/history_dev_list/status/filter/(?P<status>.+)/$```
