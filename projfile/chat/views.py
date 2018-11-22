from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse
from home.models import chat_vocab_t
from home.models import vocab_freq_central
from home.models import vocab_freq_north
from home.models import vocab_freq_south
from home.models import vocab_freq_east
from home.models import vocab_freq_west
from django.db.models import Count
import mysql.connector

# Create your views here.

def chat(request):
    data = chat_vocab_t.objects.values('vocab').annotate(frequency=Count('vocab')).order_by('-frequency')[:30]
    return render(request, 'chat/chat.html', {'data': data
    })

def room(request, room_name):
    if(room_name == 'Central'):
        data = vocab_freq_central.objects.values('vocab','frequency').order_by('-frequency')[:30]
    elif(room_name == 'North'):	
        data = vocab_freq_north.objects.values('vocab','frequency').order_by('-frequency')[:30]
    elif(room_name == 'South'): 	
        data = vocab_freq_south.objects.values('vocab','frequency').order_by('-frequency')[:30]
    elif(room_name == 'East'):	
        data = vocab_freq_east.objects.values('vocab','frequency').order_by('-frequency')[:30]
    else:	
        data = vocab_freq_west.objects.values('vocab','frequency').order_by('-frequency')[:30]
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)), 'data':data
    })

