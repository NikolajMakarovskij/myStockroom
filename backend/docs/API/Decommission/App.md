# ***App Decommission***

## App
:::src.decommission.apps.DecommissionConfig

## Admin

### Decommission
:::src.decommission.admin.DecommissionAdmin
:::src.decommission.admin.CategoryDecAdmin

### Disposal
:::src.decommission.admin.DisposalAdmin
:::src.decommission.admin.CategoryDisAdmin

## Urls

### Decommission

1. ```decom/```
2. ```decom/search```
3. ```decom/category/<slug:category_slug>```
4. ```decom/add/<uuid:device_id>/```
5. ```decom/remove/<uuid:devices_id>/```
6. ```decom/export/```
7. ```decom/export/category/<slug:category_slug>```

### Disposal

1. ```disposal/```
2. ```disposal/search```
3. ```disposal/category/<slug:category_slug>```
4. ```disposal/add/<uuid:devices_id>/```
5. ```disposal/remove/<uuid:devices_id>/```
6. ```disposal/export```
7. ```disposal/export/category/<slug:category_slug>```
