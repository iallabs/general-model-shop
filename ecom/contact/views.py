from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


from .form import ContactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print(request.POST)
        name = form.cleaned_data['name']
        comment  = form.cleaned_data['comment']
        subject = 'Message from Epsirial'
        message = '%s %s' %(comment, name)
        emailForm = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailForm, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for the message, we will get right back to you!"
        form = None

    context = {'title':title, 'form':form, 'confirm_message':confirm_message, }
    template = 'contact.html'
    return render(request,template,context)
