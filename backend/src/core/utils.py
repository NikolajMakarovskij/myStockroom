class ModelMixin:
    """
    Mixin with methods from models
    """

    def get_all_fields(self):
        """
        Returned list all fields from model. Used in DetailView
        """
        fields = []
        expose_fields = ["id", "slug"]
        for f in self._meta.fields:  # type: ignore[attr-defined]
            fname = f.name
            # added selectable lists with get_xyz_display()
            get_choice = "get_" + fname + "_display"
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # Views all fields
            if f.editable and value and f.name not in expose_fields:
                fields.append(
                    {
                        "label": f.verbose_name,
                        "name": f.name,
                        "value": value,
                    }
                )
        return fields
