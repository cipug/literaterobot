# Generated by Django 2.2.4 on 2019-11-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190819_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='attended',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
