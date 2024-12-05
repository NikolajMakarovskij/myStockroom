# ***App Device***

## App
:::src.device.apps.DeviceConfig

## Admin

### Device
:::src.device.admin.DeviceAdmin
:::src.device.admin.DeviceCatAdmin

## Urls

### Device

 1. ```/```
 2. ```search/```
 3. ```category/<slug:category_slug>/```
 4. ```category/search/<slug:category_slug>/```
 5. ```(?P<pk>[-\w]+)$```
 6. ```create/$```
 7. ```(?P<pk>[-\w]+)/update$```
 8. ```(?P<pk>[-\w]+)/delete$```
 9. ```export/```
 10. ```export/category/<slug:category_slug>```

### REST API

1. ```api/v1/device/```
2. ```api/v1/device_cat/```
