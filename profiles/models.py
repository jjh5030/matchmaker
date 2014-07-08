from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.ForeignKey(User)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField(max_length=5)

    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.user.username


class Job(models.Model):
    user = models.ForeignKey(User)
    position = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)

    employer_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField(max_length=5)
    phone = models.CharField(max_length=20, null=True, blank=True)

    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.position