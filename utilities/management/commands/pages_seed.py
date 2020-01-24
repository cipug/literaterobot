from django.core.management.base import BaseCommand
from wagtail.core.models import Page
from events.models import EventIndexPage, Event
from home.models import HomePage

import json
import os
import sys

json_directory_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname( __file__ ))))

with open(json_directory_path + r"\legacy_site_data\old_site_data.json") as f:
    event_json = json.load(f)

class Command(BaseCommand):
    help = 'Seeds the pages'

    def handle(self, *args, **kwargs):
        try:
            home_page = HomePage.objects.all()[0]
            home_page.title = "CIPUG home page"
            home_page.body = "Hello from the Channel Island Python User Group"
            home_page.seo_title = "CIPUG home page"
            home_page.save()
    
            self.stdout.write(self.style.SUCCESS('Home page created!'))

            event_index_page = EventIndexPage(
                title = "Events",
                intro = "All the CIPUG events",
                slug = "jersey-events",
            )
            home_page.add_child(instance=event_index_page)

            self.stdout.write(self.style.SUCCESS('Event index page created!'))

            number_of_events = 8

            for n in range(number_of_events):
                event = Event(
                    slug = str(n+1),
                    title = 'Meet up no. {}'.format(str(n+1)),
                    date = event_json["date"][str(n)],
                    place = event_json["place"][str(n)],
                    agenda = event_json["agenda"][str(n)],
                    notes = event_json["notes"][str(n)],
                    resources = event_json["resources"][str(n)],
                    attended = event_json["attended"][str(n)],
                )
                event_index_page.add_child(instance=event) 
                self.stdout.write(self.style.SUCCESS('Event detail page no. {} created!'.format(str(n))))

            self.stdout.write(self.style.SUCCESS('Woop woop!'))

        except:
            self.stdout.write(self.style.ERROR(f'An error occured: \n {sys.exc_info()[0]}\n{sys.exc_info()[1]}'))
