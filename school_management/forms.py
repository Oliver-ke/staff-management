from builtins import range

from django import forms
from django.template.defaultfilters import length

#importing models
from .models import A_staff
from .models import None_A_staff

# form for academic staffs
class A_staff_Form(forms.ModelForm):
    class Meta:
        model = A_staff
        fields = [
            'name',
            'dFirstAppointment',
            'rank',
            'qualification',
            'salaryGLevel',
            'step',
            'yLastPromotion',
            'pressentYear',
            'teachingE',
            'publicationS',
            'responsibilityS',
            'avater',
            'pub',
            'faculty',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'dFirstAppointment': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'date of first appointment'}),
            'rank': forms.Select(attrs={'class': 'form-control', 'placeholder': 'rank'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'qualification'}),
            'salaryGLevel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'salary grade level'}),
            'step': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'step'}),
            'yLastPromotion': forms.DateInput(attrs={'class': 'form-control', 'id': 'date2', 'placeholder': 'year of last promotion'}),
            'pressentYear': forms.DateInput(attrs={'class': 'form-control','id': 'date3', 'placeholder': 'present year'}),
            'teachingE': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Teaching Effectiveness'}),
            'publicationS': forms.Select(attrs={'class': 'form-control', 'placeholder': 'publication score'}),
            'responsibilityS': forms.Select(attrs={'class': 'form-control', 'placeholder': 'responsibility score'}),
            'avater': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'profile image'}),
            'pub': forms.Textarea(attrs={'class': 'form-control'}),
            'faculty' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Faculty'}),
            }


# form for none academic staffs
class None_A_staff_Form(forms.ModelForm):
    class Meta:
        model = None_A_staff
        fields = [
            'name',
            'dFirstAppointment',
            'qualification',
            'salaryGLevel',
            'step',
            'yLastPromotion',
            'pressentYear',
            'responsibilityS',
            'a_pcRecom',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'dFirstAppointment': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'date of first appointment'}),
            'a_pcRecom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A & PC recommendation'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'qualification'}),
            'salaryGLevel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'salary grade level'}),
            'step': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'step'}),
            'yLastPromotion': forms.DateInput(attrs={'class': 'form-control', 'id': 'date2', 'placeholder': 'year of last promotion'}),
            'pressentYear': forms.DateInput(attrs={'class': 'form-control','id': 'date3', 'placeholder': 'present year'}),
            'responsibilityS': forms.Select(attrs={'class': 'form-control','placeholder':'responsibility score'}),
            }


#search form

class searchForm(forms.Form):
    name = forms.CharField(max_length=40,
            widget = forms.TextInput(attrs= {'class': 'flexsearch--input', 'placeholder':'Search Staff','label': '' }))


#for registration form
class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Adress'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confarm Password'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full Name'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name'}))
   

        
