from django.shortcuts import render
from django.conf import settings
from .forms import contactForm
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    context = { 'title': title, 'form':form} # form is needed to keep the form on the html page

    if form.is_valid():
        #print request.POST
        # print form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        subject = 'Message from django_stripe'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks"
        confirm_message = 'Thanks for the message!'
        context = {'title':title, 'confirm_message':confirm_message}
    #context = locals() # use dictionary up top instead
    template = 'contact.html'
    return render(request, template, context)