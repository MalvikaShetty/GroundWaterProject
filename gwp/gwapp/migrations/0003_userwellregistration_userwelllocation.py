# Generated by Django 3.2.4 on 2021-09-16 19:34

import django.contrib.gis.db.models.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gwapp', '0002_auto_20210916_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwellregistration',
            name='userWelllocation',
            field=django.contrib.gis.db.models.fields.PointField(default=django.utils.timezone.now, srid=4326),
            preserve_default=False,
        ),
    ]
