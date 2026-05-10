from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactForm, ContactMessage
from product.models import Product, Category


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    products=Product.objects.all()
    categorys=Category.objects.all()
    context = {'setting':setting
               ,'page':'home'
               ,'products':products
               ,'categorys':categorys}
    return render(request,'home/index.html',context)

def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,'page':'aboutus'} #burada hangi sayafaya ilettiğimizi belli etmek amaçlı page parametreside gönderebiliriz
    return render(request,'home/aboutus.html',context)


def contactus(request):
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Mesjaınız iletildi.Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')


    setting = Setting.objects.get(pk=1)

    form = ContactForm
    context={'setting':setting,'form':form  }
    return render(request, 'home/contact.html', context)