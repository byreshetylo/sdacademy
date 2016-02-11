# -*- coding: utf-8 -*-

from django.shortcuts import render
from math import sqrt, fabs


def quadratic_results(request):
    a_data = check_value(request.GET.get('a', ''), True)
    b_data = check_value(request.GET.get('b', ''))
    c_data = check_value(request.GET.get('c', ''))
    if a_data['error'] == '' and b_data['error'] == '' and c_data['error'] == '':
        d_data = d_calculate(a_data['value'], b_data['value'], c_data['value'])
    else:
        d_data = {'d': '', 'd_desc': ''}
    context = {
        'a_value': a_data['value'],
        'b_value': b_data['value'],
        'c_value': c_data['value'],
        'd_value': d_data['d'],
        'd_details': d_data['d_desc'],
        'a_error': a_data['error'],
        'b_error': b_data['error'],
        'c_error': c_data['error'],
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
        d_desc = u'Квадратное уравнение имеет два действительных корня: x1 = %.2f, x2 = %.2f' % (x1, x2)
    return {'d': d, 'd_desc': d_desc}


def check_value(in_value, first=False):
    error = ''

    if in_value == '':
        value = in_value
        error = u'коэффициент не определен'
    else:
        try:
            value = int(in_value)
        except ValueError:
            value = in_value
            error = u'коэффициент не целое число'
            return {'value': value, 'error': error}

        if value == 0 and first is True:
            error = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    return {'value': value, 'error': error}

