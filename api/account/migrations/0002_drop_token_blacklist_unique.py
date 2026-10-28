# account/migrations/0002_drop_token_blacklist_unique.py
from django.db import migrations

TABLE = "token_blacklist_blacklistedtoken"

DROP_UNIQUE = f"""
DECLARE @name sysname, @sql nvarchar(max);
SELECT @name = name FROM sys.key_constraints
WHERE parent_object_id = OBJECT_ID('{TABLE}') AND type = 'UQ';
IF @name IS NOT NULL
BEGIN
    SET @sql = N'ALTER TABLE {TABLE} DROP CONSTRAINT ' + QUOTENAME(@name);
    EXEC sp_executesql @sql;
END
"""


def drop_unique(apps, schema_editor):
    if schema_editor.connection.vendor == "microsoft":
        schema_editor.execute(DROP_UNIQUE)


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
        ("token_blacklist", "0007_auto_20171017_2214"),
    ]

    run_before = [
        ("token_blacklist", "0008_migrate_to_bigautofield"),
    ]

    operations = [
        migrations.RunPython(drop_unique, migrations.RunPython.noop),
    ]