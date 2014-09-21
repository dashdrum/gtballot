# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
                ('ticket_mate', models.CharField(max_length=100, null=True, blank=True)),
                ('incumbent', models.BooleanField(default=False)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('view_candidate', 'View Candidate'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['govt_unit', 'name'],
                'permissions': (('view_district', 'View District'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
                ('election_date', models.DateField()),
            ],
            options={
                'ordering': ['election_date'],
                'permissions': (('view_election', 'View Election'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GovernmentalUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('view_unit', 'View Governmental Unit'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('view_muni', 'View Municipality'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(to='ballot.District')),
            ],
            options={
                'ordering': ['district', 'name'],
                'permissions': (('view_office', 'View Office'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('view_party', 'View Party'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Precinct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('prec_number', models.CharField(max_length=2)),
                ('polling_location', models.CharField(max_length=100)),
                ('municipality', models.ForeignKey(to='ballot.Municipality')),
            ],
            options={
                'ordering': ['municipality', 'prec_number'],
                'permissions': (('view_precinct', 'View Precinct'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('district', models.ForeignKey(to='ballot.District')),
                ('election', models.ForeignKey(to='ballot.Election')),
            ],
            options={
                'ordering': ['title'],
                'permissions': (('view_proposal', 'View Proposal'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('votes_allowed', models.IntegerField(default=1)),
                ('election', models.ForeignKey(to='ballot.Election')),
                ('office', models.ForeignKey(to='ballot.Office')),
            ],
            options={
                'ordering': ['election', 'office'],
                'permissions': (('view_race', 'View Race'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on', editable=False)),
                ('updated_on', models.DateTimeField(verbose_name='updated on', editable=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('view_level', 'View Unit Level'),),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='governmentalunit',
            name='unit_level',
            field=models.ForeignKey(to='ballot.UnitLevel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='govt_unit',
            field=models.ForeignKey(to='ballot.GovernmentalUnit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='precints',
            field=models.ManyToManyField(to='ballot.Precinct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(to='ballot.Party'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='race',
            field=models.ForeignKey(to='ballot.Race'),
            preserve_default=True,
        ),
    ]
