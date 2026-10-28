# account/migrations/0003_restore_token_blacklist_unique.py
from django.db import migrations

TABLE = "token_blacklist_blacklistedtoken"

ADD_UNIQUE = f"""
IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes i
    JOIN sys.index_columns ic ON ic.object_id = i.object_id AND ic.index_id = i.index_id
    JOIN sys.columns c ON c.object_id = ic.object_id AND c.column_id = ic.column_id
    WHERE i.object_id = OBJECT_ID('{TABLE}')
      AND i.is_unique = 1
      AND i.is_primary_key = 0
      AND c.name = 'token_id'
)
    ALTER TABLE {TABLE} ADD CONSTRAINT {TABLE}_token_id_uniq UNIQUE (token_id);
"""


def add_unique(apps, schema_editor):
    if schema_editor.connection.vendor == "microsoft":
        schema_editor.execute(ADD_UNIQUE)


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_drop_token_blacklist_unique"),
        ("token_blacklist", "0013_alter_blacklistedtoken_options_and_more"),
    ]

    operations = [
        migrations.RunPython(add_unique, migrations.RunPython.noop),
    ]