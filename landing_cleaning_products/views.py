from django.shortcuts import render, redirect
from .forms import ZipCodeForm
from zipcodes.models import ZipCodes

def index(request):
    form = ZipCodeForm()
    if request.method == 'POST':
        zipcode = request.POST.get('zipcode')
        
        if ZipCodes.objects.filter(zipcode__contains=zipcode).exists():
            return redirect('check/')
        
        else:
            return render(request, 'index.html', {
                'uncover': True
            })

    return render(request, 'index.html', {
        'form': form,
    })

def check(request):

    return render(request, 'check.html', {
        'check': True
    })