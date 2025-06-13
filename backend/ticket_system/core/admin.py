from django.contrib import admin
from .models import *

admin.site.register(Visitor)
admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(EventTicket)

