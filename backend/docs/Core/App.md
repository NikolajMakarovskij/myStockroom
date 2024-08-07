# ***App Core***

## App
:::src.core.apps.CoreConfig

## Admin
consts

```python
admin.site.site_title = "admin panel title"
admin.site.site_header = "admin panel header"
```

## Urls

```python
urlpatterns = [
    # главная
    path("", IndexView.as_view(), name="index")
]
```





