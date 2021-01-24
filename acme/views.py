from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorators import *
from .filter import *
# email
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string, get_template
# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def index(request):
    ammos = Ammonition.objects.all()
    return render(request, "index.html", {"ammos": ammos})


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def applications(request):
    return render(request, "applications.html")


@login_required(login_url='login')
@allowed_user(allowed_role=['CO', 'QM'])
def qmpermission(request):
    notpermitted = Issue.objects.filter(qm_permission=False).order_by('-date')
    context = {'nonpermits': notpermitted}
    return render(request, "qmpermission.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'QM', 'CO'])
def issue(request):
    forms = IssueForm()
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            amount = form.cleaned_data.get('amount')
            stock = form.cleaned_data.get('stock')
            if amount < stock.amount:
                return redirect('/issue')
            else:
                issue.delete()
                messages.info(
                    request, "Amount can not be more than the stock.Input Again")
    notpermitted = Issue.objects.filter(qm_permission=False).order_by('-date')
    permitteds = Issue.objects.filter(qm_permission=True).order_by('-date')
    myFilters = IssueFilter(request.GET, queryset=permitteds)
    permitteds = myFilters.qs
    context = {'forms': forms,
               'nonpermits': notpermitted, 'permits': permitteds, 'myFilters': myFilters}
    return render(request, "issue.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['QM'])
def permit(request, pk):
    issue = Issue.objects.get(id=pk)
    amount = issue.amount
    forms = IssueUpdateForm(instance=issue)
    if request.method == 'POST':
        form = IssueUpdateForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('/stock')
    serial = issue.stock.serial
    stock = Stock.objects.get(serial=serial)
    stock.amount = stock.amount - amount
    stock.deficiency = stock.auth-stock.amount
    stock.save()
    context = {'forms': forms}
    return render(request, "permit.html", context)


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            messages.info(request, "Worng password, login again")
            return redirect('/login')
    else:
        return render(request, "login.html")


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def service(request):
    ammo_des = Ammo.objects.all()
    myFilters = AmmoFilter(request.GET, queryset=ammo_des)
    ammo_des = myFilters.qs
    context = {"ammo_des": ammo_des, 'myFilters': myFilters}
    return render(request, "service.html", context)


@login_required(login_url='login')
# @allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def logout(request):
    auth.logout(request)
    return redirect('/index')


@unauthenticated_user
def register(request):
    forms = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Authorizer.objects.create(user=user)
            return HttpResponse("Wait for the varification Email.")
        else:
            messages.warning(request, "Wrong Credentials.")
    context = {'forms': forms}
    return render(request, 'register.html', context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def signup(request):
    authorizer = request.user.authorizer
    forms = AuthorizerForm(instance=authorizer)
    context = {'forms': forms}
    if request.method == 'POST':
        f = AuthorizerForm(request.POST, instance=authorizer)
        if f.is_valid():
            f.save()
            return redirect("index")
    return render(request, "signup.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def inout(request):
    forms = InOutForm()
    if request.method == 'POST':
        f = InOutForm(request.POST)
        if f.is_valid:
            f.save()
            return redirect('/inout')
    inouts = InOut.objects.all()
    myFilters = InOutFilter(request.GET, queryset=inouts)
    inouts = myFilters.qs
    context = {'forms': forms, 'inouts': inouts, 'myFilters': myFilters}
    return render(request, "inout.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def weather(request):
    forms = WeatherForm()
    if request.method == 'POST':
        f = WeatherForm(request.POST)
        if f.is_valid:
            f.save()
            return redirect('/weather')
    weathers = Weather.objects.all()
    myFilters = WeatherFilter(request.GET, queryset=weathers)
    weathers = myFilters.qs
    context = {'forms': forms, 'weathers': weathers, 'myFilters': myFilters}
    return render(request, "weather.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def stock(request):
    forms = StockForm()
    stocks = Stock.objects.all()
    myFilters = StockFilter(request.GET, queryset=stocks)
    stocks = myFilters.qs
    if request.method == 'POST':
        f = StockForm(request.POST)
        if f.is_valid:
            stock = f.save()
            auth = f.cleaned_data.get('auth')
            amount = f.cleaned_data.get('amount')
            ammo1 = f.cleaned_data.get('ammo')
            coy1 = f.cleaned_data.get('coy')
            coy_stock = Stock.objects.filter(ammo=ammo1)
            coy_count = coy_stock.filter(coy=coy1).count()
            #ammo_count = Stock.objects.filter(ammo=ammo1).count()
            #total = ammo_count * coy_count
            if coy_count > 1:
                stock.delete()
                messages.warning(request, "Stock Exists.")
            elif amount < auth:
                stock.deficiency = auth - amount
                stock.save()
                return redirect('/stock')
            else:
                stock.delete()
                messages.warning(request, "Wrong Input.")
        else:
            messages.warning(request, "Wrong Input.")
    #stocks = Stock.objects.all()
    # for stock in stocks:
    #    stock.deficiency = stock.auth - stock.amount
    context = {'forms': forms, 'stocks': stocks,
               'myFilters': myFilters}
    return render(request, "stock.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def issuer(request):
    issuers = Issuer.objects.all()
    myFilters = IssuerFilter(request.GET, queryset=issuers)
    issuers = myFilters.qs
    forms = IssuerForm()
    if request.method == 'POST':
        f = IssuerForm(request.POST)
        if f.is_valid:
            issue = f.save()
            #leadger = Leadger.objects.create(issue=issue)
            #date = f.cleaned_data.get('date')
            #leadger.date = date
            # leadger.save()
            return redirect('/issuer')
    context = {'forms': forms, 'issuers': issuers, 'myFilters': myFilters}
    return render(request, "issuer.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'QM', 'CO'])
def deposit(request):
    forms = DepositForm()
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save()
            extra = form.cleaned_data.get('extra')
            empty = form.cleaned_data.get('empty_case')
            stock = form.cleaned_data.get('stock')
            issue = form.cleaned_data.get('issue')
            stock.amount = stock.amount + extra
            stock.save()
            deposit.deficiency = issue.amount - extra - empty
            deposit.save()
            return redirect('/deposit')
        else:
            messages.warning(request, "Wrong Credentials.")
    deposits = Deposit.objects.all()
    myFilters = DepositFilter(request.GET, queryset=deposits)
    deposits = myFilters.qs
    context = {'forms': forms, 'deposits': deposits, 'myFilters': myFilters}
    return render(request, "deposit.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def demand(request):
    forms = DemandForm()
    if request.method == 'POST':
        f = DemandForm(request.POST)
        if f.is_valid:
            demand = f.save()
            stocks = f.cleaned_data.get('stock')
            amount = 0
            for stock in stocks:
                amount = amount + stock.deficiency
            demand.amount = amount
            demand.save()
            return redirect('/demand')
    demands = Demand.objects.all()
    myFilters = DemandFilter(request.GET, queryset=demands)
    demands = myFilters.qs
    context = {'forms': forms, 'demands': demands, 'myFilters': myFilters}
    return render(request, "demand.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def demanddetails(request, pk):
    demand = Demand.objects.get(id=pk)
    stocks = demand.stock.all()
    if request.method == 'POST':
        return redirect('/applications')
    context = {'demands': demand, 'stocks': stocks}
    return render(request, "demanddetails.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def stockupdate(request, pk):
    stock = Stock.objects.get(id=pk)
    auth = stock.auth
    forms = StockForm1(instance=stock)
    if request.method == 'POST':
        f = StockForm1(request.POST, instance=stock)
        if f.is_valid():
            stock = f.save()
            amount = f.cleaned_data.get('amount')
            if amount < auth:
                stock.deficiency = auth - amount
                stock.save()
                return redirect('/stock')
            else:
                stock.delete()
                messages.warning(request, "Wrong Input.")
        else:
            messages.warning(request, "Wrong Input.")
    context = {'forms': forms, 'stock': stock}
    return render(request, 'stockupdate.html', context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def lot(request):
    forms = LotForm()
    lots = Lot.objects.all()
    #myFilters = LotFilter(request.GET, queryset=lots)
    #lots = myFilters.qs
    if request.method == 'POST':
        form = LotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lot')
    context = {'forms': forms, 'lots': lots}
    return render(request, "lot.html", context)


@login_required(login_url='login')
@allowed_user(allowed_role=['KOTENCO', 'CO', 'QM'])
def line(request):
    forms = LineForm()
    lines = Line.objects.all()
    myFilters1 = LineFilter(request.GET, queryset=lines)
    lines = myFilters1.qs
    ammolines = AmmoLine.objects.all()
    myFilters = AmmoLineFilter(request.GET, queryset=ammolines)
    ammolines = myFilters.qs
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            line = form.save()
            lot = form.cleaned_data.get('lot')
            ammoline = form.cleaned_data.get('ammoline')
            line.amount = lot.amount
            line.save()
            ammoline1 = AmmoLine.objects.get(id=ammoline.id)
            ammoline1.amount = ammoline1.amount + line.amount
            ammoline1.save()
            #leadger = Leadger.objects.create(line=line)
            #date = f.cleaned_data.get('date_added')
            #leadger.date = date
            # leadger.save()
            return redirect('/line')
    context = {'forms': forms, 'lines': lines, 'ammolines': ammolines,
               'myFilters': myFilters, 'myFilters1': myFilters1}
    return render(request, "line.html", context)


def leadger(request):
    #leadgers = Leadger.objects.all()
    context = {}
    return render(request, 'leadger.html', context)


@login_required(login_url='login')
@admin_only
def sendemail(request):
    template = render_to_string('template.html')
    email_subject = "Verification"
    if request.method == 'POST':
        email1 = request.POST['email']
        send_mail(
            email_subject,
            template,
            settings.EMAIL_HOST_USER,
            [email1],
            fail_silently=False,
        )
        messages.info(request, "Confirmation Email Sent")
        return redirect('sendemail')
    # email1.send()
    return render(request, "sendemail.html")
