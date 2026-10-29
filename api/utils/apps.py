from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_inactive_permissions(sender, **kwargs):
    from django.apps import apps
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from utils.models import TimeStampedModel

    for model in apps.get_models():
        if not issubclass(model, TimeStampedModel):
            continue
        ct = ContentType.objects.get_for_model(model)
        Permission.objects.update_or_create(
            content_type=ct,
            codename=f"view_inactive_{model._meta.model_name}",
            defaults={"name": f"Can see inactive {model._meta.verbose_name_plural}"},
        )
class UtilsConfig(AppConfig):
    name = 'utils'

    def ready(self):
        post_migrate.connect(create_inactive_permissions, sender=self)
