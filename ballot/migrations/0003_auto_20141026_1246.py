# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0002_auto_20141024_0034'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Municipality',
            new_name='PrecinctArea',
        ),
        migrations.AlterModelOptions(
            name='precinct',
            options={'permissions': (('view_precinct', 'View Precinct'),), 'ordering': ['prec_area', 'prec_number']},
        ),
        migrations.RenameField(
            model_name='precinct',
            old_name='municipality',
            new_name='prec_area',
        ),
    ]
