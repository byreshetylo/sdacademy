# -*- coding: utf-8 -*-

from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10, label=u'коэффициент a')
    b = forms.CharField(max_length=10, label=u'коэффициент b')
    c = forms.CharField(max_length=10, label=u'коэффициент c')

    def clean_a(self):
        a = self.cleaned_data['a']
        return self.check_value(a, first=True)

    def clean_b(self):
        b = self.cleaned_data['b']
        return self.check_value(b)

    def clean_c(self):
        c = self.cleaned_data['c']
        return self.check_value(c)

    def check_value(self, in_value, first=False):
        if in_value == '':
            raise forms.ValidationError(u'коэффициент не определен')
        else:
            try:
                value = int(in_value)
            except ValueError:
                raise forms.ValidationError(u'коэффициент не целое число')

            if value == 0 and first is True:
                raise forms.ValidationError(u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
            return value

        return in_value
