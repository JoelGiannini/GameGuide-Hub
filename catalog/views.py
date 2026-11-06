from django.shortcuts import render
from .models import Platform

def catalog_view(request):
    platforms = Platform.objects.all()
    return render(request, 'catalog/catalog_list.html', {'platforms': platforms})
