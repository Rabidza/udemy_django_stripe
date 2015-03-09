from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length = 1200)
    description = models.TextField(default='description default')
    
    #models below are for demonstration purposes -- asked to remove them by lecturer
    #location = models.CharField(max_length = 1200, default='My location', blank=True)
    #job = models.CharField(max_length = 1200, null=True)
    ## Remember when you add any more models you have to run
    ## python manage.py makemigrations
    ## python manage.py migrate


    def __unicode__(self):
        # unicode is part of the class -- indented the method
        return self.name 
