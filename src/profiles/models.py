from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 1200)
    description = models.TextField()

def __unicode__(self):
        return self.name # Why the double indentation????!!
