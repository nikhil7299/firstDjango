from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpRequest

from contact_form_app.form import ContactForm

def contact_form(request:HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'thank_you_form.html')
        else:
            form= ContactForm()
            return render(request,'InValid Data',)
    else:
        form= ContactForm()
        return render(request,'contact_form.html',{'form':form})