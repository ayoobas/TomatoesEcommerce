# Generated by Django 5.1.1 on 2024-10-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]