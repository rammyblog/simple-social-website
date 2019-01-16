from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User as user_

# Create your models here.
class User(user_, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
