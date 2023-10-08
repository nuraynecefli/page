from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForms
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    skills = Skills.objects.all()
    contacts = ContactForms()
    
    context = {
        
        "home":home,
        "about":about,
        "skills":skills,
        'contacts':contacts,
            
    }
    
    return render(request,'index.html', context)




def save_contacts(request):
    contact_forms = ContactForms(request.POST)
    
    if contact_forms.is_valid():
        subject = "Contact form submitted"
        
        body = {
            "name": contact_forms.cleaned_data['name'],
            "email": contact_forms.cleaned_data['email'],
            "message": contact_forms.cleaned_data['message']
            
        }
        
        message = '\n'.join(body.values())
        
        send_mail(subject,message,'test@gmail.com',['nuraynecefli2001@gmail.com'],fail_silently=False)
        
    return redirect('index',)

