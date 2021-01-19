from django.shortcuts import render,HttpResponse

# Create your views here.
from home.models import Settings
from projects.models import Projects

def project(request):
  settings = Settings.objects.get(pk = 1)
  projects = Projects.objects.all().filter(status = True)
  
  context = {'setting': settings, 'project': project, 'projects': projects}

  return render(request, 'indexProject.html', context)

def continueProject(request):
  settings = Settings.objects.get(pk = 1)
  
  projects = Projects.objects.all().filter(status = False)
  
  context = {'setting': settings, 'projects': projects}

  return render(request, 'continueProject.html', context)
