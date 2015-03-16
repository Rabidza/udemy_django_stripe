from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length = 1200)
    description = models.TextField(default='description default')
    # link auth_user to profile
    # Foreign key
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    #models below are for demonstration purposes -- asked to remove them by lecturer
    #location = models.CharField(max_length = 1200, default='My location', blank=True)
    #job = models.CharField(max_length = 1200, null=True)
    ## Remember when you add any more models you have to run
    ## python manage.py makemigrations
    ## python manage.py migrate


    def __unicode__(self):
        # unicode is part of the class -- indented the method
        return self.name

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

def my_callback(sender, request, user, **kwargs):
    idStripe, created = userStripe.objects.get_or_create(user=user)
    if created:
        print 'created for %s' %(user.username)

    userProfile, isCreated = profile.objects.get_or_create(user=user)
    if isCreated:
        userProfile.name = user.username
        userProfile.save()

user_logged_in.connect(my_callback)
