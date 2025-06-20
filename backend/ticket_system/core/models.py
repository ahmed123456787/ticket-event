from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager



class User(AbstractBaseUser, PermissionsMixin):
    """
    Unified user model supporting roles: organizer, admin, attendee, visitor.
    """
    ROLE_CHOICES = (
        ('organizer', 'Organizer'),
        ('admin', 'Admin'),
        ('visitor', 'Visitor'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        self.is_staff = self.role in ['admin', 'organizer']
        super().save(*args, **kwargs)


class Event(models.Model):
    """
    Model representing an event in the ticket system.
    """
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    nb_tickets = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    image_banner = models.ImageField(upload_to='event_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    discount_for_tickets = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    attendees = models.ManyToManyField(
        User,
        through='EventTicket',
        related_name='attended_events'
    )

    def __str__(self):
        return self.name

    @property
    def available_tickets(self):
        return self.nb_tickets - self.tickets.filter(is_used=False).count()


class EventTicket(models.Model):
    """
    Model representing an event ticket in the ticket system.
    """
  

    ticket_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    purshased_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_used = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    price_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.ticket_code


class EventStats(models.Model):
    """
    Model for tracking event statistics and analytics data.
    """
    ACTION_TYPES = (
        ('view', 'View'),
        ('click', 'Click'),
        ('share', 'Share'),
        ('purchase_start', 'Purchase Started'),
        ('purchase_complete', 'Purchase Completed'),
        ('email_open', 'Email Opened'),
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='stats')
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='actions')
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    referrer = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['event', 'action_type']),
            models.Index(fields=['timestamp']),
        ]
        verbose_name = 'Event Statistic'
        verbose_name_plural = 'Event Statistics'

    def __str__(self):
        return f"{self.event.name} - {self.action_type} - {self.timestamp}"
