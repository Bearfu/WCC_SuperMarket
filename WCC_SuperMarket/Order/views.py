from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def Test(request):
    return HttpResponse("Hello Now_a_Magic")
