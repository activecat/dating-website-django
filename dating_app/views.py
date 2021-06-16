from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'dating_app/index.html')
    # return HttpResponse("Hello, welcome to dating website 1234")
