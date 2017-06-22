from django.shortcuts import render

# Create your views here.

def make_investigator(request):
    return render(request, 'characterbirther/make_investigator.html', {})
