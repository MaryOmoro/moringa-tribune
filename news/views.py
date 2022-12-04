from django.http import HttpRespose

# Create your views here.
def welcome(request):
    return HttpRespose('Welcome to Moringa Tribune')
