# Generated by Django 3.2.14 on 2023-03-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki_energie', '0021_alter_geraete_geraete_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='mst_messtelle',
            fields=[
                ('id', models.AutoField(db_column='id',
                 primary_key=True, serialize=False)),
                ('zaehler_nr', models.CharField(
                    blank=True, max_length=20, null=True)),
                ('zaehler_typ', models.CharField(
                    blank=True, max_length=20, null=True)),
                ('zaehler_einheit', models.BigIntegerField(blank=True, null=True)),
                ('zaehler_name', models.TextField(max_length=128)),
                ('log_datum_erfasst', models.DateTimeField(blank=True, null=True)),
                ('log_datum_ltz_aend', models.DateTimeField(blank=True, null=True)),
                ('log_user', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='geraete',
            old_name='geraete_id',
            new_name='id',
        ),
        # migrations.RemoveField(
        #     model_name='raumliste',
        #     name='raum_id',
        # ),
        migrations.AddField(
            model_name='geraete',
            name='connection',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='geraete',
            name='hw_hersteller',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='geraete',
            name='ip_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='geraete',
            name='ip_port',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='geraete',
            name='put_request',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='raumliste',
            name='id',
            field=models.AutoField(
                db_column='Id', default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sensorvaluetypes',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
