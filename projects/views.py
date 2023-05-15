from django.shortcuts import render
from django.http import HttpResponse

ProjectsList = [ # this is another global function that can be called apon in the function as 'ProjectList'
                {
                'id':'1',
                'title': "Ecommerce Website",
                'description':'fully funtioncal ecommerce website'
                },
                {
                'id':'2',
                'title': "portfolio Website",
                'description':'this was a project where i built out my portfolio'
                },
                {
                'id':'3',
                'title': "social network",
                'description':'awesome open source project i am still working on'
                },
                {
                'id':'4',
                'title': "samuel",
                'description':'big up this man ye'
                },

        ]

def projects(request):
        page = 'projects'
        number = 10
        context = {'page':page,'number':number, 'projects':ProjectsList} # other variables are called here in one dict
        # the above are parameters that can be passed through to the function and recieved to be passed through. acting as a variable that can now be used in the templates file to be shown in the page
        return render(request, 'projects/projects.html', context)# projects.html is a template that is being used
# if more info is wanted for this function, go into projects.html and change there.

def project(request,pk):
        projectObj = None
        for i in ProjectsList:
                if i['id'] == pk:
                        projectObj = i
                        # this loop is going through what is entered in the url i.e 1 and referencing is to the projectlist variable so it can be outputted in the page
        return render(request, 'projects/single_project.html', {'project':projectObj})# this is another function that refers to single_project.html


