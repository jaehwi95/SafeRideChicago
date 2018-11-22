from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponse
from home.models import crime_t,new_format
from .form import CrimeForm
from .form import SearchForm
from django.db.models import Count,Sum
from collections import defaultdict
from collections import Counter
from datetime import datetime
from operator import itemgetter
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.



def base_page(request):
    latlon = crime_t.objects.values('latitude', 'longitude').exclude(longitude = None)[:1000]
    results = crime_t.objects.values('address', 'date', 'description', 'location_desc', 'latitude', 'longitude')[:1000]
    return render(request, 'base_page.html',{'data': latlon, 'results': results})


def list(request):
    result = crime_t.objects.all().order_by('-id')
    paginator = Paginator(result, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    data = paginator.get_page(page)
    return render(request, 'list.html', {'data': data})

def delete(request,id):
    fb = crime_t.objects.get(id=id)
    fb.delete()
    return redirect('/login/showmylist')

def create(request):
    if request.method=='POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            p = crime_t(description=form.cleaned_data['description'], location_desc=form.cleaned_data['location_desc'], address=form.cleaned_data['address'])
            authorname = User.objects.get(username=request.user.username)
            p.author = authorname
            p.save()
        return redirect('/report/list')
    else:
        form = CrimeForm()
    return render(request,'create.html',{'form' : form})

def edit(request, id):
    fb = crime_t.objects.get(id=id)
    if request.method=='POST':
        form = CrimeForm(request.POST, instance=fb)
        if form.is_valid():
            form.save()
        return redirect('/login/showmylist')
    else:
        form = CrimeForm()
    return render(request, 'create.html', {'form': form})

def search(request):
    C = crime_t.objects.all()
    if request.method=='POST':
        fb = SearchForm(request.POST)
        if fb.is_valid():
            data = C
            if fb.returnlocation() != ['']:
                tempa = fb.returnlocation()
                data = data.filter(location_desc__in = tempa)
            # print(fb.data['Description'])
            result_2 = new_format.objects.all().values().order_by('description','new_date')
            if fb.returndesc() != ['']:
                tempa = fb.returndesc()
                data = data.filter(description__in = tempa)
                result_2 = result_2.filter(description__in = tempa).order_by('description','new_date')
                print("check")
            year1,year2 = fb.returndate()
            if year1 is not None and year2 is not None:
                data = data.filter(date__range=(year1, year2))
            result = data.values('description').annotate(Count('description')).order_by('-description__count')
            c = {}
            d = {}
            for data_1 in result:
                c[data_1['description']] = []
                if data_1['description'] == 'REDLIGHT VIOLATION':
                    continue
                #if data_1 ['description__count'] < 500 :
                #    etc[0] = etc[0] + data_1['description__count']
                #    continue
                d[data_1['description']] = data_1['description__count']
            for data_2 in result_2:
                try:
                    c[data_2['description']].append((data_2['new_date'],data_2['new_count']))
                except:
                    continue
            val = {}
            for i in c.keys():
                if len(c[i]) != 0:
                    val[i] = c[i]
            data_2 = data.all()[:69]
            return render(request, 'search.html', {'form': fb , 'data':data , 'pie': d,'line' : val,'data_2':data_2})
        else:
            return HttpResponse("Please write correct input")
    else:
        form = SearchForm()
        data = CrimeForm()
    return render(request, 'search.html', {'form': form , 'crime': data})

def simple(request):
    return render(request, 'simple.html')

def base(request):
    return render(request, 'base.html')


def geo(request):
    result = crime_t.objects.all().order_by('-id')[:30]
    return render(request, 'geo.html', {'data': result})
