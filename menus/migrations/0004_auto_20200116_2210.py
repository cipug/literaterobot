# Generated by Django 2.2.9 on 2020-01-16 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20200116_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='menu',
            new_name='page',
        ),
    ]