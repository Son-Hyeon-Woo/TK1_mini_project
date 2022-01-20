from platform import java_ver
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Place
import random
def quiz(request):
    place_list = Place.objects.all()
    num = random.randrange(0,len(place_list))
    answer = place_list[num]
    return render(
        request,
        'mapquiz/quiz.html',
        {'data': place_list,
         'ans':answer,}
    )

def index(request):
    
    return render(request, 'mapquiz/index.html')
