from django.shortcuts import render

# Create your views here.
def hari(request):
    return render(request,'hari.html')

def dhoni(request):
    return render(request,'dhoni.html')