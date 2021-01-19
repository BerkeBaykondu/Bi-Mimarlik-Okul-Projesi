from django.shortcuts import render,HttpResponse

# Create your views here.
from home.models import Settings, About

def index(request):
  settings = Settings.objects.get(pk = 1)
  about = About.objects.all().filter(status = True)
  
  context = {'setting': settings, 'about': about}

  return render(request, 'index.html', context)

