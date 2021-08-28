from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    homepage = models.URLField(null=True, blank=True)
    display_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    REQUIRED_FIELDS = ['age']
