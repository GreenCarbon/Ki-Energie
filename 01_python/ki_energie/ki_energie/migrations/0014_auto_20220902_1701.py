# Generated by Django 3.2.14 on 2022-09-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki_energie', '0013_auto_20220902_0516'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='raumliste',
            name='etage_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='raumliste',
            name='gebaeude_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        
    ]
