# Generated by Django 5.1.1 on 2024-11-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Lagos', 'Lagos'), ('Ondo', 'Ondo'), ('Ekiti', 'Ekiti'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Kwara', 'Kwara')], max_length=100),
        ),
    ]
