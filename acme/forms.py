from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AuthorizerForm(ModelForm):
    class Meta:
        model = Authorizer
        fields = "__all__"
        exclude = ['user']


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = "__all__"
        exclude = ['qm_permission']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = "__all__"
        exclude = ['deficiency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class IssueUpdateForm(ModelForm):
    class Meta:
        model = Issue
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"
        exclude = ['deficiency', 'serial']


class StockForm1(ModelForm):
    class Meta:
        model = Stock
        fields = ["amount"]


class IssuerForm(ModelForm):
    class Meta:
        model = Issuer
        fields = "__all__"


class InOutForm(ModelForm):
    class Meta:
        model = InOut
        fields = ['date', 'number', 'name', 'rk',
                  'coy', 'reason', 'in_time', 'out_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'in_time': forms.TimeInput(attrs={'type': 'time'}),
            'out_time': forms.TimeInput(attrs={'type': 'time'})
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }


class DemandForm(ModelForm):
    class Meta:
        model = Demand
        fields = '__all__'
        exclude = ['co_permission', 'amount', 'serial']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class LotForm(ModelForm):
    class Meta:
        model = Lot
        fields = "__all__"


class LineForm(ModelForm):
    class Meta:
        model = Line
        fields = "__all__"
        exclude = ['amount', 'ammo']

        widgets = {
            'date_added': forms.DateInput(attrs={'type': 'date'})
        }
