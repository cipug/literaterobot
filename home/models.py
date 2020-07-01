from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock



class HomePage(Page):
    
    body = StreamField([
        ('jumbotron', blocks.RawHTMLBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    subpage_types = [
        'home.HomePage',
        'home.BasicPage',
    ]

    parent_page_type = [
        'wagtailcore.Page'
    ]



class BasicPage(Page):

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    subpage_types = [
        'home.BasicPage',
    ]

    parent_page_type = [
        'wagtailcore.Page'
    ]
