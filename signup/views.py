import signup
from django.shortcuts import render

# Create your views here.
def user_signup(request):
    return render(request, 'signup/register.html')