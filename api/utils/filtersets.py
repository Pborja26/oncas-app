from django.db.models import Value
from django.db.models.functions import Concat
from django_filters import rest_framework as filters
from utils import models


def can_see_inactive_records(user, model):
    if not user or not user.is_authenticated:
        return False
    opts = model._meta
    return user.has_perm(f"{opts.app_label}.view_inactive_{opts.model_name}")

class BaseAuditFilterSet(filters.FilterSet):
    active = filters.BooleanFilter(help_text="Defaults to true. Empty value returns all records (requires permission).")
    created_at = filters.IsoDateTimeFromToRangeFilter(help_text="Use created_at_after / created_at_before.")
    updated_at = filters.IsoDateTimeFromToRangeFilter(help_text="Use updated_at_after / updated_at_before.")
    created_by = filters.CharFilter(method="filter_user", help_text="User id of part of the user's full name.")
    updated_by = filters.CharFilter(method="filter_user", help_text="User id of part of the user's full name.")

    class Meta: 
        fields = [
            "id",
            "active",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]

    def filter_user(self, queryset, name, value):
        value = value.strip()
        if value.isdigit():
            return queryset.filter(**{f"{name}_id": int(value)})

        full_name = f"{name}_full_name"

        return queryset.annotate(
            **{full_name: Concat(f"{name}__first_name", Value(" "), f"{name}__last_name")}
        ).filter(**{f"{full_name}__icontains": value})

    def __init__(self, data=None, queryset=None, *, request=None, **kwargs):
        if data is not None:
            data = data.copy()
            user = getattr(request, "user", None)
            if can_see_inactive_records(user, self._meta.model):
                data.setdefault("active", "true")
            else:
                data["active"] = "true"
        super().__init__(data, queryset, request=request, **kwargs)

class ThemeFilterSet(BaseAuditFilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    color = filters.CharFilter(lookup_expr="icontains")
    category = filters.CharFilter(method="filter_category")
    class Meta(BaseAuditFilterSet.Meta):
        model = models.Theme
        fields = BaseAuditFilterSet.Meta.fields + [
            "name",
            "color",
            "category"
        ]

    def filter_category(self, queryset, name, value):
        value = value.strip()
        if value.isdigit():
            return queryset.filter(category_id=int(value))
        return queryset.filter(category__name__icontains=value)
