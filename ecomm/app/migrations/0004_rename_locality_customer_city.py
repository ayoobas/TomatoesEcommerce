# Generated by Django 5.1.1 on 2024-10-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_name_customer_firstname_customer_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='locality',
            new_name='city',
        ),
    ]