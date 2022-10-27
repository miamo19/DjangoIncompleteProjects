from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def achiffe(request):
    return render(request, "index.html")
