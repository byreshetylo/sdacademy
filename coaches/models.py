from django.db import models
from django.contrib.auth.models import User


class Coach(User):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=25)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username