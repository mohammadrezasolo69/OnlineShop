from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, phone_number, full_name, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')

        if not phone_number:
            raise ValueError('The given phone number must be set')

        if not full_name:
            raise ValueError('The given full name must be set')

        email = self.normalize_email(email).lower()
        user = self.model(email=email, phone_number=phone_number, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_number, full_name, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)

        return self._create_user(email, phone_number, full_name, password, **extra_fields)

    def create_superuser(self, email, phone_number, full_name, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, full_name, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="The entered mobile phone is not valid")

    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=12, validators=[phone_regex])
    full_name = models.CharField(max_length=100, verbose_name='Full name')
    avatar = models.ImageField(upload_to='uploads/accounts/avatar', blank=True, null=True)
    beo = models.TextField(blank=True, null=True)  # todo : change CKEditor

    is_verify = models.DateTimeField(null=True, blank=True, default=None)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "full_name"]

    def __str__(self):
        return self.email
