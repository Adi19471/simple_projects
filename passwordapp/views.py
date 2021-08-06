from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'password/home.html')





def way(request):
    return HttpResponse("adi")
#
# def homes():
#     s = {'keys':"ADI"}
#     return HttpResponse("DJANGO ADI",{s:s})
