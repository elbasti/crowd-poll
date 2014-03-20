from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lead(models.Model):
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.email