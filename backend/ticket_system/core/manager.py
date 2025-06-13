from django.contrib.auth.models import UserManager



class CustomUserManager(UserManager):
    """
    Custom user manager for the ticket system.
    This manager can be extended to include custom user creation logic.
    """

    def create_user(self, name, email=None, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not name:
            raise ValueError('The given username must be set')
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email=None, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, email, password, **extra_fields)