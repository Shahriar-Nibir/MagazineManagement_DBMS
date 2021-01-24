from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login, name="login"),
    path("service", views.service, name="service"),
    path("register", views.register, name="register"),
    path("signup", views.signup, name="signup"),
    path("inout", views.inout, name="inout"),
    path("logout", views.logout, name="service"),
    path("weather", views.weather, name="weather"),
    path("issuer", views.issuer, name="issuer"),
    path("applications", views.applications, name="applications"),
    path("issue", views.issue, name="issue"),
    path("qmpermission", views.qmpermission, name="qmpermission"),
    path("permit/<str:pk>", views.permit, name="permit"),
    path("deposit", views.deposit, name="deposit"),
    path("demand", views.demand, name="demand"),
    path("demanddetails/<str:pk>", views.demanddetails, name="demanddetails"),
    path("stockupdate/<str:pk>", views.stockupdate, name="stockupdate"),
    path("lot", views.lot, name="lot"),
    path("line", views.line, name="line"),
    path("leadger", views.leadger, name="leadger"),
    path("sendemail", views.sendemail, name="sendemail"),
    path("stock", views.stock, name="stock")
]
