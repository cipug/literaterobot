from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    subpage_types = [
        'home.HomePage',
        'events.EventIndexPage',
    ]

    parent_page_type = [
        'wagtailcore.Page'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
