from rest_framework import viewsets
from utils import filtersets
from utils import models
from utils import serializers

class InactiveProtectedMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if not filtersets.can_see_inactive_records(self.request.user, qs.model):
            qs = qs.filter(active=True)
        return qs

class BaseAuditViewSet(InactiveProtectedMixin, viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user
        )
    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user
        )

class ThemeViewSet(BaseAuditViewSet):
    queryset = models.Theme.objects.select_related("category")
    filterset_class = filtersets.ThemeFilterSet
    serializer_class = serializers.ThemeSerializer
