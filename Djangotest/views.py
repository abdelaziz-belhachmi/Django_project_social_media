from django.shortcuts import render

def home_view(request):
    context = {}  # You can pass context data to the template if needed
<<<<<<< Updated upstream
    return render(request, 'HTML/home-extended.html', context)
=======
    return render(request, 'HTML/home.html', context)

def index_view(request):
    context = {}  # You can pass context data to the template if needed
    return render(request,'HTML/index.html',context)
>>>>>>> Stashed changes
