# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0004_auto_20141031_0055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['sort_order', 'govt_unit', 'name'], 'permissions': (('view_district', 'View District'),)},
        ),
        migrations.AlterModelOptions(
            name='election',
            options={'ordering': ['sort_order', 'election_date'], 'permissions': (('view_election', 'View Election'),)},
        ),
        migrations.AlterModelOptions(
            name='governmentalunit',
            options={'ordering': ['sort_order', 'name'], 'permissions': (('view_unit', 'View Governmental Unit'),)},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'ordering': ['sort_order', 'district', 'name'], 'permissions': (('view_office', 'View Office'),)},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'verbose_name_plural': 'parties', 'ordering': ['sort_order', 'name'], 'permissions': (('view_party', 'View Party'),)},
        ),
        migrations.AlterModelOptions(
            name='precinct',
            options={'ordering': ['sort_order', 'prec_area', 'prec_number'], 'permissions': (('view_precinct', 'View Precinct'),)},
        ),
        migrations.AlterModelOptions(
            name='precinctarea',
            options={'ordering': ['sort_order', 'name'], 'permissions': (('view_muni', 'View Municipality'),)},
        ),
        migrations.AlterModelOptions(
            name='proposal',
            options={'ordering': ['sort_order', 'title'], 'permissions': (('view_proposal', 'View Proposal'),)},
        ),
        migrations.AlterModelOptions(
            name='race',
            options={'ordering': ['sort_order', 'election', 'office'], 'permissions': (('view_race', 'View Race'),)},
        ),
        migrations.AlterModelOptions(
            name='unitlevel',
            options={'ordering': ['sort_order', 'name'], 'permissions': (('view_level', 'View Unit Level'),)},
        ),
        migrations.AddField(
            model_name='candidate',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='election',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='governmentalunit',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='office',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='precinct',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='precinctarea',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proposal',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='race',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unitlevel',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
