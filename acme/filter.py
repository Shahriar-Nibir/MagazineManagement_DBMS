import django_filters
from django_filters import *
from .models import *
from django import forms


class StockFilter(django_filters.FilterSet):
    ammo = ModelChoiceFilter(field_name='ammo', queryset=Ammo.objects.all())
    coy = CharFilter(field_name='coy', lookup_expr='icontains')
    #start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    #end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Stock
        fields = ['ammo', 'coy']


class AmmoFilter(django_filters.FilterSet):
    ammo_name = CharFilter(field_name='ammo_name',
                           lookup_expr='icontains', label='Name')
    #start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    #end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Ammo
        fields = ['ammo_name']


class IssuerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',
                      lookup_expr='icontains', label='Name')
    no = CharFilter(field_name='no',
                    lookup_expr='icontains', label='Number')
    coy = CharFilter(field_name='coy',
                     lookup_expr='icontains', label='Company')
    rk = CharFilter(field_name='rk',
                    lookup_expr='icontains', label='Rank')
    #start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    #end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Issuer
        fields = ['name', 'no', 'coy', 'rk']


class IssueFilter(django_filters.FilterSet):
    ammo = ModelChoiceFilter(field_name='ammo', queryset=Ammo.objects.all())
    issuer = ModelChoiceFilter(
        field_name='issuer', queryset=Issuer.objects.all())
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Issue
        fields = ['ammo', 'issuer', 'date']


class DepositFilter(django_filters.FilterSet):
    issue = ModelChoiceFilter(
        field_name='issue', queryset=Issue.objects.all())
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Deposit
        fields = ['issue', 'date']


class DemandFilter(django_filters.FilterSet):
    stock = ModelMultipleChoiceFilter(
        field_name='stock', queryset=Stock.objects.all())
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Demand
        fields = ['stock', 'date']


class InOutFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',
                      lookup_expr='icontains', label='Name')
    no = CharFilter(field_name='no',
                    lookup_expr='icontains', label='Number')
    date = DateFilter(field_name='date', label='Date')

    class Meta:
        model = InOut
        fields = ['name', 'no', 'date']


class WeatherFilter(django_filters.FilterSet):
    date = DateFilter(field_name='date', label='Date')
    temperature = CharFilter(field_name='temperature',
                             lookup_expr='icontains', label='Temperature')
    humidity = CharFilter(field_name='humidity',
                          lookup_expr='icontains', label='Humidity')

    class Meta:
        model = Weather
        fields = ['date', 'temperature', 'humidity']


class LotFilter(django_filters.FilterSet):
    no = CharFilter(field_name='no', lookup_expr='icontains', name="Lot No")
    #ammo = ModelChoiceFilter(field_name='ammo', queryset=Ammo.objects.all())

    class Meta:
        model = Lot
        fields = ['no']


class AmmoLineFilter(django_filters.FilterSet):
    ammo = ModelChoiceFilter(field_name='ammo', queryset=Ammo.objects.all())
    linename = ModelChoiceFilter(
        field_name='linename', queryset=LineName.objects.all())

    class Meta:
        model = AmmoLine
        fields = ['ammo', 'linename']


class LineFilter(django_filters.FilterSet):
    ammoline = ModelChoiceFilter(
        field_name='ammoline', queryset=AmmoLine.objects.all())
    lot = ModelChoiceFilter(
        field_name='lot', queryset=Lot.objects.all())

    class Meta:
        model = Line
        fields = ['ammoline', 'lot']
