from django.core.management.base import BaseCommand
from menus.models import Menu, MenuItem
import sys

class Command(BaseCommand):
    help = 'Seeds the main-nav menu'

    def handle(self, *args, **kwargs):
        try:
            menu = Menu.objects.create(title='main-nav',slug='main-nav')
            link1 = MenuItem.objects.create(link_title='test',link_url='https://www.google.com',open_in_new_tab=True,page=menu)
            link2 = MenuItem.objects.create(link_title='Test Event Index',link_url='/test-event-index/',open_in_new_tab=False,page=menu)

            self.stdout.write(self.style.SUCCESS('Menu created, you trooper!'))
        
        except:
            self.stdout.write(self.style.ERROR(f'An error occured: \n {sys.exc_info()[0]}\n{sys.exc_info()[1]}'))



