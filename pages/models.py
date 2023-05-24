from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255) # creates text field with max 255 characters
    lastname = models.CharField(max_length=255) # creates text field with max 255 characters