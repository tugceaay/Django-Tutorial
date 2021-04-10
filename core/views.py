from django.shortcuts import render
from django.http import HttpResponse

def wellcome(request):
    return HttpResponse("Hoşgeldiniz!")

def goodbye(request, name):
    if "Fatih" not in name:
        return HttpResponse("Hoşçakal {}".format(name))
    else:
        return HttpResponse("Sen kalbimden başka bir yere gidemezsin my biricik husband")

def add(request, numbers):
    numbers_list = numbers.split(",")
    total = 0
    for i in numbers_list:
        if i.isdigit():
            total = total + int(i)
        else:
            return HttpResponse("Düzgün formatta sayı girin!")
    return HttpResponse("Sayıların toplamı: {}".format(total))




