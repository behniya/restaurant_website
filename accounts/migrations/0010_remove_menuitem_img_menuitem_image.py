# Generated by Django 5.1.1 on 2024-09-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='img',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]
