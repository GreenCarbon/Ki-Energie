# Generated by Django 3.2.14 on 2022-09-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki_energie', '0017_auto_20220911_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raumliste',
            old_name='log_erzeugt_am',
            new_name='log_datum_vom',
        ),
        migrations.RemoveField(
            model_name='raumliste',
            name='log_letzte_änderung_am',
        ),
        migrations.AddField(
            model_name='raumliste',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        
    ]
