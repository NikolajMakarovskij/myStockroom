# ***Core***

## App

### App
:::src.core.apps.CoreConfig

### Admin
consts

```python
admin.site.site_title = "admin panel title"
admin.site.site_header = "admin panel header"
```

### urls

```python
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

### IndexView
:::src.core.views.IndexView

## tests
:::src.core.tests.test_login.auto_login_user
:::src.core.tests.test_login.test_view_unauthorized
:::src.core.tests.test_login.test_view_as_admin
:::src.core.tests.test_urls.test_url_exists_at_desired_location
:::src.core.tests.test_urls.test_urls