# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encoder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ip_monitor', models.CharField(blank=True, max_length=16, null=True)),
                ('source_main', models.CharField(blank=True, max_length=25, null=True)),
                ('source_backup', models.CharField(blank=True, max_length=25, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'encoder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=60, null=True)),
                ('start_date', models.IntegerField(blank=True, null=True)),
                ('end_date', models.IntegerField(blank=True, null=True)),
                ('create_date', models.IntegerField(blank=True, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'event',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('last_update', models.IntegerField(blank=True, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('descr', models.CharField(blank=True, max_length=255, null=True)),
                ('encoder', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.Encoder')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.Event')),
            ],
            options={
                'db_table': 'event_monitor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('active', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service_check',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='eventmonitor',
            name='service_check',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.ServiceCheck'),
        ),
        migrations.AlterUniqueTogether(
            name='eventmonitor',
            unique_together=set([('id', 'event', 'encoder', 'service_check')]),
        ),
    ]