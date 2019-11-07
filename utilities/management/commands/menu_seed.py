from django.core.management.base import BaseCommand
from menus.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Seeds the main-nav menu'

    def handle(self, *args, **kwargs):
        menu = Menu(title='main-nav',slug='main-nav')
        menu.save()
        link1 = MenuItem(link_title='test',link_url='https://www.google.com',open_in_new_tab=True,page=menu)
        link1.save()

