from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=256, blank=True)
    level = models.CharField(max_length=1, blank=True,
        choices=[
            ('L', 'Local'),
            ('R', 'Regional'),
            ('N','National'),
            ('I', 'International')
        ]
    )
    locations = models.ManyToManyField('cities_light.City')


    def __str__(self):
        return str(self.user.get_full_name())


class Skill(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ])
    city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.get_full_name())
    

class Resource(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    resourceID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    quantity = models.CharField(max_length=32)
    city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
    ward = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.name)