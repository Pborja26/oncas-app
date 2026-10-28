from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TimeStampedModel(models.Model):
    id = models.AutoField(primary_key=True, help_text="Primary key, unique for everi record in each model.")
    active = models.BooleanField(default=True, help_text="Simple boolean to help filter inactive records that are no longer in use.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the record was last updated.")

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

class BaseAuditModel(TimeStampedModel):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="%(class)s_created_by", help_text="User who created the record.")
    updated_by =models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="%(class)s_updated_by", help_text="User who last updated the record.")

    class Meta:
        abstract = True
