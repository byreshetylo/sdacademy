# -*- coding: utf-8 -*-

from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10, label=u'коэффициент a')
    b = forms.CharField(max_length=10, label=u'коэффициент b')
    c = forms.CharField(max_length=10, label=u'коэффициент c')
