from django.shortcuts import render, HttpResponse

# Create your views here.
def principal(request):
    return render(request, "core/principal.html")
def about(request):
    return render(request, "core/about.html")