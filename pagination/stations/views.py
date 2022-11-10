from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    st_list = []
    with open('data-398-2018-08-30.csv', encoding = "UTF-8") as f:
        reader = csv.DictReader(f)
        st_list = list(reader)
    
        page_number = int(request.GET.get('page', 1))
        pag = Paginator(st_list, 10)
        page = pag.get_page(page_number)
        

        context = {
            'bus_stations': st_list,
            'page': page
        }
        return render(request, 'stations/index.html', context)
