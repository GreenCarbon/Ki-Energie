# Generated by Django 3.2.14 on 2022-09-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki_energie', '0014_auto_20220902_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raumliste',
            old_name='server_name',
            new_name='server_id',
        ),
        migrations.RemoveField(
            model_name='raumliste',
            name='etage',
        ),
        
        
        
    ]
