from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


#create user manager here
class UserProfileManager(BaseUserManager):
    """help django work with our custom user model """

    def create_user(self,email,name,password=None):
        """create a new user profile object """
        if not email:
            raise ValueError('user must have an email address valid.')
            email = self.normalize_email(email)
            
            user = self.model(email=email, name=name)

            user.set_password(password)
            user.save(using=self._db)

            return user
    def create_superuser(self,email,name,password):
        """create and save a new superuser with given details """
        user = self.create_user(email,name,password)

        user.is_superuser = True

        user.is_staff = True

        user.save(using=self._db)






#create ypur user profile here
class Userprofile(AbstractBaseUser, PermissionsMixin):
    """  represent user profile inside a system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self):
        """used to get user full name """
        return self.name

    def get_short_name(self):
        """used to get user shortname"""
        return self.name

    def __str__(self):
        """django uses this when it needs to convert the object to string """
        return self.email
    






    
