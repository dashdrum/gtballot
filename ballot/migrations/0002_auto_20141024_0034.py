# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='municipality',
            options={'permissions': (('view_muni', 'View Municipality'),), 'verbose_name_plural': 'Municipalities', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'permissions': (('view_party', 'View Party'),), 'verbose_name_plural': 'parties', 'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(null=True, to='ballot.Party', blank=True),
            # preserve_default=True,
        ),
    ]
