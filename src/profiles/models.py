from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.Charfield(max_length = 1200)

def __unicode__(self):
        return self.name
