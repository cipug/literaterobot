from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from datetime import date

class EventIndexPage(Page):
    intro = RichTextField(blank=True)

    subpage_types = [
        'events.EventPage',
    ]

    parent_page_type = ['home.HomePage']

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)

        # Get all published event pages as a queryset
        all_event_pages = EventPage.objects.live().order_by('-date')

        paginator = Paginator(all_event_pages, 3) # show 3 events per page

        page = request.GET.get('page')

        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)
        
        context['events'] = events
        context['mark'] = 'mark'

        return context

class EventPage(Page):

    date = models.DateField("Event date")
    place = models.CharField(max_length=250)
    agenda = RichTextField(blank=True)
    notes = RichTextField(blank=True)
    resources = RichTextField(blank=True)
    attended = models.IntegerField(blank=True, null=True, help_text="Please enter the number of people that attended, or leave blank")

    search_fields = Page.search_fields + [
        index.SearchField('agenda'),
        index.SearchField('notes'),
        index.SearchField('resources'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('place'),
        FieldPanel('agenda', classname="full"),
        FieldPanel('notes', classname="full"),
        FieldPanel('resources', classname="full"),
        FieldPanel('attended'),
    ]

    def get_context(self, request):
        context = super(EventPage, self).get_context(request)
        context['today'] = date.today()
        return context

