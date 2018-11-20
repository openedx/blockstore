# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('entity_type', models.CharField(max_length=180)),
                ('external_id', models.CharField(max_length=180)),
            ],
            options={
                'verbose_name_plural': 'Entities',
                'db_table': 'tagstore_entity',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tag', max_length=180)),
                ('path', models.CharField(db_index=True, max_length=180)),
            ],
            options={
                'db_table': 'tagstore_tag',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=180)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tagstore_django.Entity')),
            ],
            options={
                'verbose_name_plural': 'Taxonomies',
                'db_table': 'tagstore_taxonomy',
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='taxonomy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagstore_django.Taxonomy'),
        ),
        migrations.AddField(
            model_name='entity',
            name='tags',
            field=models.ManyToManyField(to='tagstore_django.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('taxonomy', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='entity',
            unique_together=set([('entity_type', 'external_id')]),
        ),
    ]
