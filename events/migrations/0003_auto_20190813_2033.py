# Generated by Django 2.2.4 on 2019-08-13 19:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('events', '0002_blogpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='EventPage',
        ),
    ]
