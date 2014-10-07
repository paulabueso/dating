from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=35)

    def __unicode__(self):
        return self.city


class User(AbstractUser):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    GENDER_CHOICES = (
                        ('M', 'Male'),
                        ('F', 'Female'),
                     )
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    paid = models.BooleanField(default=False)

    profile_image = models.ImageField(upload_to='img', height_field=None, width_field=None,
                                      max_length=1000, default="../static/img/couple.png")
    location = models.ForeignKey(Location, null=True, blank=True)

    # def __unicode__(self):
    #     return self.name
#
#
# class Interest(models.Model):
#     name = models.CharField(max_length=30)
#     user = models.ManyToManyField(User, related_name="interest")
#
#     def __unicode__(self):
#         return self.name


class Messages(models.Model):
    message = models.TextField(max_length=300)
    sender = models.ForeignKey(User, related_name="message_sender")
    receiver = models.ForeignKey(User, related_name="message_receiver")

    def __unicode__(self):
        return self.message