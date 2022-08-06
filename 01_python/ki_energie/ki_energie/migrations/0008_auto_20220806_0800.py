# Generated by Django 3.2.14 on 2022-08-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki_energie', '0007_erganalyse_messwert_id'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='Workparameter',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=50, null=True)),
                ('modul', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('subname', models.CharField(blank=True, max_length=100, null=True)),
                ('typ', models.BigIntegerField()),
                ('int_val', models.BigIntegerField(null=True)),
                ('str_val', models.CharField(blank=True, max_length=256, null=True)),
                ('text_val', models.TextField(blank=True, null=True)),
                ('date_val', models.DateField(null=True)),
                ('time_val', models.TimeField(null=True)),
                ('datetime_val', models.DateTimeField(null=True)),
                ('comment', models.TextField()),
                ('log_datum_vom', models.DateTimeField(blank=True, null=True)),
            ],
        ),
       
        migrations.AddField(
            model_name='geraete',
            name='get_request',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        
        
    ]