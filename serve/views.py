from django.shortcuts import render

# Create your views here.
def projects(request):
    context={'services' : 'active'}
    return render(request,'serve/project.html',context)
