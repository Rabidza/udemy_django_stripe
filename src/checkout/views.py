from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

secretKey = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        print token
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request, template, context)