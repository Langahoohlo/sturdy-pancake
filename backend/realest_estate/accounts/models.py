from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# Cutosm User Account Model
class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """Create a new user account"""
        if not email:
            raise ValueError("User must have an email address")
        
        if not name:
            raise ValueError("User must have a name")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save() 

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """Database model for User Account"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self ):
        return self.email
