from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Event, EventTicket, EventStats

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email', 'name', 'role', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email', 'name', 'role')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('id',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'location', 'nb_tickets', 'organizer', 'ticket_price', 'discount_for_tickets')
    search_fields = ('name', 'location', 'organizer__name', 'organizer__email')
    list_filter = ('date', 'is_published')

@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket_code', 'event', 'user', 'purshased_date', 'is_used', 'price_paid', 'status')
    search_fields = ('ticket_code', 'event__name', 'user__name', 'user__email')
    list_filter = ('is_used', 'event', 'status')

@admin.register(EventStats)
class EventStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'action_type', 'user', 'timestamp', 'ip_address')
    list_filter = ('action_type', 'event', 'timestamp')
    search_fields = ('event__name', 'user__name', 'user__email', 'ip_address')
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)

