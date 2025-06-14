from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'location', 'nb_tickets', 'organizer', 'ticket_price', 'discount_for_tickets')
    search_fields = ('name', 'location', 'organizer__name')
    list_filter = ('date', 'organizer')

@admin.register(Organization)
class OrganizationAdmin(UserAdmin):
    model = Organization
    list_display = ('id', 'name', 'email', 'is_staff', 'is_active')
    search_fields = ('name', 'email')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('id',)

@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket_code', 'event', 'visitor', 'purshased_date', 'is_used', 'price_paid')
    search_fields = ('ticket_code', 'event__name', 'visitor__name')
    list_filter = ('is_used', 'event')

