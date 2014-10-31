# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0003_auto_20141026_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precinctarea',
            options={'ordering': ['name'], 'permissions': (('view_muni', 'View Municipality'),)},
        ),
        migrations.RenameField(
            model_name='district',
            old_name='precints',
            new_name='precincts',
        ),
    ]
