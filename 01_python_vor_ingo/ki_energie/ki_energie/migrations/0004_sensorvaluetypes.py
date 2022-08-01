# Generated by Django 3.1.14 on 2022-05-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki_energie', '0003_auto_20220512_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorValueTypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('kategorie', models.CharField(blank=True, max_length=1, null=True)),
                ('kategorie_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sub_kategorie', models.CharField(blank=True, max_length=1, null=True)),
                ('sub_kategorie_name', models.CharField(blank=True, max_length=50, null=True)),
                ('soll_ist_value', models.CharField(blank=True, max_length=1, null=True)),
                ('inside_outside', models.CharField(blank=True, max_length=1, null=True)),
                ('pri_sec', models.CharField(blank=True, max_length=1, null=True)),
                ('medium', models.CharField(blank=True, max_length=20, null=True)),
                ('bemerkung', models.CharField(blank=True, max_length=500, null=True)),
                ('log_erzeugt_am', models.DateTimeField(blank=True, null=True)),
                ('log_letzte_aenderung_am', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
