from django.db import models

class Contact(models.Model):
    your_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    dogs_name = models.CharField(max_length=50, null=False, blank=False)
    dogs_age = models.CharField(max_length=50, null=False, blank=False)
    dogs_breed = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=2000, null=False, blank=False)

    def __str__(self):
        return self.contact
