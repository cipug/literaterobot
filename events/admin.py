from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Event
# Register your models here.
class EventAdmin(ModelAdmin):
    model = Event
    menu_label = "Events"
    menu_icon = "date"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer=False
    list_display = ("title","date","place")
    search_fields = ("date", "place")

modeladmin_register(EventAdmin)
