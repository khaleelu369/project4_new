from django.shortcuts import render
# Create your views here.
def mycart(request):
    return render(request, 'sellertemplates/mycart.html')
def myorder (request):
    return render(request, 'sellertemplates/myorder.html')    