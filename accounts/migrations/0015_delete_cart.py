# Generated by Django 5.1.1 on 2024-10-01 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
