# Generated by Django 3.2.4 on 2021-09-16 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gwapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GroundWaterLevelPostMonsoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearOfInput', models.IntegerField()),
                ('dateOfInput', models.DateField()),
                ('noOfObservationWells', models.IntegerField()),
                ('postMonsoonLevel', models.DecimalField(decimal_places=3, max_digits=20)),
                ('totalWaterRechargedFromRainfall', models.DecimalField(decimal_places=3, max_digits=20)),
                ('totalWaterRechargedFromSurfaceWater', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='GroundWaterLevelPreMonsoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearOfInput', models.IntegerField()),
                ('dateOfInput', models.DateField()),
                ('noOfObservationWells', models.IntegerField()),
                ('preMonsoonLevel', models.DecimalField(decimal_places=3, max_digits=20)),
                ('totalWaterRechargedFromRainfall', models.DecimalField(decimal_places=3, max_digits=20)),
                ('totalWaterRechargedFromSurfaceWater', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Landuse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('cultivatedLandArea', models.DecimalField(decimal_places=3, max_digits=20)),
                ('uncultivatedLandArea', models.DecimalField(decimal_places=3, max_digits=20)),
                ('noncultivableLandArea', models.DecimalField(decimal_places=3, max_digits=20)),
                ('forestArea', models.DecimalField(decimal_places=3, max_digits=20)),
                ('otherLandUseArea', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adults', models.IntegerField()),
                ('under18', models.IntegerField()),
                ('seniorCitizen', models.IntegerField()),
                ('female', models.IntegerField()),
                ('male', models.IntegerField()),
                ('other', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearOfInput', models.IntegerField()),
                ('dateOfInput', models.DateField()),
                ('averageRainfall', models.DecimalField(decimal_places=3, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talukaName', models.CharField(max_length=500)),
                ('districtName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.district')),
            ],
        ),
        migrations.CreateModel(
            name='UserBorewellRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userBorewellID', models.CharField(max_length=200, null=True)),
                ('userBorewellType', models.CharField(max_length=50)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.userbasic')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villageName', models.CharField(max_length=500)),
                ('districtName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.district')),
                ('talukaName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.taluka')),
            ],
        ),
        migrations.AddField(
            model_name='userwellregistration',
            name='dateOfWellRegistration',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userwellregistration',
            name='userWellActiveOrInact',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userwellregistration',
            name='userWellDugDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userwellregistration',
            name='wellOwner',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserWaterUsage',
        ),
        migrations.AddField(
            model_name='rainfall',
            name='villageName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.taluka'),
        ),
        migrations.AddField(
            model_name='population',
            name='villageName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.taluka'),
        ),
        migrations.AddField(
            model_name='landuse',
            name='villageName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.taluka'),
        ),
        migrations.AddField(
            model_name='groundwaterlevelpremonsoon',
            name='villageName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.taluka'),
        ),
        migrations.AddField(
            model_name='groundwaterlevelpostmonsoon',
            name='villageName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwapp.taluka'),
        ),
    ]
