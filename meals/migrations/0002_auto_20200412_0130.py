# Generated by Django 3.0.5 on 2020-04-11 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='FIELDNAME',
            new_name='price',
        ),
    ]