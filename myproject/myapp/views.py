from django.shortcuts import render

# Homepage view
def home(request):
    return render(request, 'myapp/home.html')
