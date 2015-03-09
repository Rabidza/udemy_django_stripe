from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 1200)
    description = models.TextField(default='description default')
    ## Remember when you add any more models you have to run
    ## python manage.py makemigrations
    ## python manage.py migrate

    def __unicode__(self):
        # unicode is part of the class -- indented the method
        return self.name 
