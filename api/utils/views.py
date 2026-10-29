from rest_framework import viewsets
from utils.filtersets import can_see_inactive_records

class InactiveProtectedMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if not can_see_inactive_records(self.request.user, qs.model):
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
