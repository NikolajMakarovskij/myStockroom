from import_export import fields, resources

from decommission.models import Decommission


class DecommissionResource(resources.ModelResource):

    class Meta:
        model = Decommission
        fields = [
            'stock_model__name',
            'stock_model__categories__name',
            'stock_model__serial',
            'stock_model__serialImg',
            'stock_model__invent',
            'stock_model__inventImg',
            'stock_model__hostname',
            'stock_model__ip_address',
            'stock_model__login',
            'stock_model__pwd',
            'stock_model__workplace__name',
            'stock_model__accessories__name',
            'stock_model__consumable__name',
            'stock_model__manufacturer__name',
            'stock_model__description',
            'stock_model__note'
        ]
