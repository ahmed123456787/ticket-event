from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import CustomUserManager 

class Organization(AbstractBaseUser, PermissionsMixin):
    """
    Model representing an organizer in the ticket system.
    This model extends AbstractBaseUser to allow custom user management.
    """
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super().save(*args, **kwargs)



class Visitor(models.Model):
    """
    Model representing a visitor in the ticket system.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Model representing an event in the ticket system.
    """
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    nb_tickets = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(Organization, on_delete=models.CASCADE,related_name='events')
    discount_for_tickets = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    visitors = models.ManyToManyField(
        Visitor,
        through='EventTicket',
        related_name='events'
    )

    def __str__(self):
        return self.name

    @property
    def available_tickets(self):
        """
        Returns the number of available tickets for the event.
        """
        return self.nb_tickets - self.tickets.filter(is_used=False).count()



    

class EventTicket(models.Model):
    """
    Model representing a evnt ticket in the ticket system.
    """
    ticket_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    purshased_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_used = models.BooleanField(default=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE,related_name='tickets')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    price_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.ticket_code
