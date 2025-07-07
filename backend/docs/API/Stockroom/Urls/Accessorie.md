# ***Accessories***

## REST API

### Stockroom

1. ```api/stockroom/stock_acc_list/```
2. ```api/stockroom/stock_acc_cat_list/```

### Methods

1. ```api/stockroom/add_to_stock_accessories/```
2. ```api/stockroom/add_to_device_accessories/```
3. ```api/stockroom/remove_from_stock_accessories/```

### Export

1. ```api/stockroom/accessories/export/```
2. ```api/stockroom/accessories/export/category/<slug:category_slug>```
3. ```api/stockroom/accessories/consumption/export/```
4. ```api/stockroom/accessories/consumption/export/category/<slug:category_slug>```

### History

1. ```api/stockroom/history_acc_list/```
2. ```api/stockroom/consumption_acc_list/```
3. ```api/stockroom/history_acc_list/filter/(?P<stock_model_id>.+)/$```
4. ```api/stockroom/history_acc_list/device/filter/(?P<deviceId>.+)/$```
