from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.
def home(request):
    return render(request,'login.html')