# ***App Counterparty***

## App
:::src.counterparty.apps.CounterpartyConfig

## Admin

### ManufacturerAdmin
:::src.counterparty.admin.ManufacturerAdmin

## Urls

```python
urlpatterns = [
    path("", CounterpartyView.as_view(), name="counterparty"),
    # Производитель
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer_list"),
    path(
        "manufacturer/search",
        ManufacturerListView.as_view(),
        name="manufacturer_search",
    ),
    re_path(
        r"^manufacturer/(?P<pk>[-\w]+)$",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail",
    ),
    re_path(
        r"^manufacturer/create/$", ManufacturerCreate.as_view(), name="new-manufacturer"
    ),
    re_path(
        r"^manufacturer/(?P<pk>[-\w]+)/update$",
        ManufacturerUpdate.as_view(),
        name="manufacturer-update",
    ),
    re_path(
        r"^manufacturer/(?P<pk>[-\w]+)/delete$",
        ManufacturerDelete.as_view(),
        name="manufacturer-delete",
    ),
]

```