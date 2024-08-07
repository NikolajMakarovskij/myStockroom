# ***Core***

## App

### App
:::src.core.apps.CoreConfig

### Admin
consts

```bash
admin.site.site_title = "admin panel title"
admin.site.site_header = "admin panel header"
```

### urls

```
urlpatterns = [
    # главная
    path("", IndexView.as_view(), name="index")
]
```

## Utils

### DataMixin
:::src.core.utils.DataMixin

### BaseModelSelect2WidgetMixin
:::src.core.utils.BaseModelSelect2WidgetMixin

### BaseSelect2MultipleWidgetMixin
:::src.core.utils.BaseSelect2MultipleWidgetMixin

### ModelMixin
:::src.core.utils.ModelMixin

### FormMessageMixin
:::src.core.utils.FormMessageMixin

## Views
:::src.core.views.IndexView