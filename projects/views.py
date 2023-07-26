from django.shortcuts import render
from projects.models import Project

def all_projects(request):
    #query db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', 
                  {'projects': projects})