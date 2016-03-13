# -*- coding: utf-8 -*-

from django.shortcuts import render
from forms import QuadraticForm
from math import sqrt, fabs


def quadratic_results(request):
    form = QuadraticForm(request.GET)
    d_data = {'d': '', 'd_desc': ''}
    if form.is_valid():
        d_data = d_calculate(form.cleaned_data['a'], form.cleaned_data['b'], form.cleaned_data['c'])
    context = {
        'd_value': d_data['d'],
        'd_details': d_data['d_desc'],
        'form': form,
    }
    return render(request, 'results.html', context)

# LoGiC goes here \|/


def d_calculate(a, b, c):
    d = pow(b, 2) - 4 * a * c
    x1 = (-b + sqrt(fabs(d))) / (2 * a)
    x2 = (-b - sqrt(fabs(d))) / (2 * a)
    if d < 0:
        d_desc = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif d == 0:
        d_desc = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x1
    else:
        d_desc = u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)
    return {'d': d, 'd_desc': d_desc}
