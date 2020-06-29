from django.db import models
from django.contrib.auth.models import User, auth


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Unique_ID = models.CharField(max_length=99999, blank=True)
    Email = models.CharField(max_length=99999, blank=True)
    Contact = models.CharField(max_length=99999, blank=True)
    Email_Verified = models.CharField(max_length=99999, blank=True, default='False')
    Phone_Verified = models.CharField(max_length=99999, blank=True, default='False' )

    def __str__(self):
        return self.user.username
