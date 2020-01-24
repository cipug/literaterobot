from django.core.management.base import BaseCommand
from wagtail.core.models import Page
from events.models import EventIndexPage, Event
from home.models import HomePage
from pathlib import Path

import json
import os
import sys

json_directory_path = Path("legacy_site_data/old_site_data1.json")

with open(json_directory_path) as f:
    event_json = json.load(f)

for key in event_json["attended"]:
    try:
        event_json["attended"][key] = int(event_json["attended"][key])
    except:
        event_json["attended"][key] = 0

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
                slug = "events",
            )
            home_page.add_child(instance=event_index_page)

            self.stdout.write(self.style.SUCCESS('Event index page created!'))

            number_of_events = 13

            for n in range(number_of_events):
                event = Event(
                    date = event_json["date"][str(n)],
                    place = event_json["place"][str(n)],
                    agenda = event_json["agenda"][str(n)],
                    notes = event_json["notes"][str(n)],
                    resources = event_json["resources"][str(n)],
                    attended = event_json["attended"][str(n)],
                )
                event_index_page.add_child(instance=event) 
                self.stdout.write(self.style.SUCCESS('Event detail page no. {} created!'.format(str(n))))

        except:
            self.stdout.write(self.style.ERROR(f'An error occured: \n {sys.exc_info()[0]}\n{sys.exc_info()[1]}'))
