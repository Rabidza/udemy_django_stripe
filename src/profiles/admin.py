from django.contrib import admin

# Register your models here.
from .models import profile, userStripe # .models (looks inside the same folder as this .py)

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, profileAdmin)

class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe

admin.site.register(userStripe, userStripeAdmin)
