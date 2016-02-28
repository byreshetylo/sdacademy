from django.shortcuts import render
from models import Coach


def detail(request, pk=0):
    coach_detail = Coach.objects.filter(pk=pk)
    if len(coach_detail) > 0:
        context = {
            'coach_detail': Coach.objects.filter(pk=pk)[0]
        }
    else:
        context = {}
    return render(request, 'coaches/detail.html', context)
