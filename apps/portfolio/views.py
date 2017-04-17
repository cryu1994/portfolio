from django.shortcuts import render

def index(request):
    return render(request, "index/index.html")
def testimonials(request):
    return render(request, "index/testimonials.html")
