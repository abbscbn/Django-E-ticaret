from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text="Selam Abbas"

    return render(request,'index.html',{'text':text})