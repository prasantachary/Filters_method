from django.shortcuts import render

# Create your views here.

def userfilters(request):
    d={'data':'Prasant Achary'}
    return render(request,'userfilters.html',d)
    
