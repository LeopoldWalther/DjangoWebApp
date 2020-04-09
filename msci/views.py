from django.shortcuts import render

# Create your views here.
def msci(request):
    return render(request, 'msci.html', {})