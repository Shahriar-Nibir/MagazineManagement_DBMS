from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ammonition(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    spl = models.BooleanField(default=False)


class Ammo(models.Model):
    ammo_name = models.CharField(max_length=100)
    itm_no = models.CharField(max_length=100)
    un_no = models.CharField(max_length=100)
    cl_div = models.CharField(max_length=100)
    m_no = models.CharField(max_length=100)

    def __str__(self):
        return self.ammo_name


class Authorizer(models.Model):
    CATEGORY = (
        ('CO', 'CO'),
        ('QM', 'QM'),
        ('KOTENCO', 'KOTENCO')
    )
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    number = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    rk = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    appointment = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name


class InOut(models.Model):
    date = models.DateField(max_length=200, null=False)
    in_time = models.TimeField(null=False)
    number = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    rk = models.CharField(max_length=200, null=True)
    coy = models.CharField(max_length=200, null=True)
    reason = models.CharField(max_length=200, null=True)
    out_time = models.TimeField(null=False)
    authorizer = models.ForeignKey(
        Authorizer, null=True, on_delete=models.CASCADE)


class Weather(models.Model):
    date = models.DateField(max_length=200, null=False)
    time = models.TimeField(null=False)
    temperature = models.CharField(max_length=200, null=True)
    humidity = models.CharField(max_length=200, null=True)


class Lot(models.Model):
    ammo = models.ForeignKey(Ammo, null=True, on_delete=models.CASCADE)
    no = models.CharField(max_length=200, null=True)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.ammo.ammo_name+"("+self.no+")"


class Stock(models.Model):
    serial = models.PositiveIntegerField(null=True)
    ammo = models.ForeignKey(Ammo, null=False, on_delete=models.CASCADE)
    coy = models.CharField(max_length=200, null=True)
    auth = models.PositiveIntegerField(null=True, default=0)
    amount = models.PositiveIntegerField(null=True, default=0)
    deficiency = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return self.ammo.ammo_name+"-coy"+self.coy


class Issuer(models.Model):
    name = models.CharField(max_length=200, null=True)
    no = models.CharField(max_length=200, null=True)
    coy = models.CharField(max_length=200, null=True)
    rk = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name+"-coy"+self.coy


class Issue(models.Model):
    issuer = models.ForeignKey(Issuer, null=False, on_delete=models.CASCADE)
    ammo = models.ForeignKey(Ammo, null=True, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, null=True, on_delete=models.CASCADE)
    lot_no = models.ForeignKey(Lot, null=True, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True, default=0)
    reason = models.CharField(max_length=200, null=True)
    date = models.DateField(max_length=200, null=False)
    qm_permission = models.BooleanField(default=False)

    def __str__(self):
        return self.issuer.name+"-Date"+str(self.date)


class Deposit(models.Model):
    date = models.DateField(null=False)
    reason = models.CharField(max_length=200, null=True)
    empty_case = models.PositiveIntegerField(null=True, default=0)
    extra = models.PositiveIntegerField(null=True, default=0)
    deficiency = models.PositiveIntegerField(null=True, default=0)
    #issuer = models.ForeignKey(Issuer, null=True, on_delete=models.CASCADE)
    issue = models.OneToOneField(Issue, null=False, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, null=True, on_delete=models.CASCADE)


class Demand(models.Model):
    serial = models.PositiveIntegerField(null=False, default=0)
    stock = models.ManyToManyField(Stock)
    date = models.DateField(null=True)
    amount = models.PositiveIntegerField(null=False, default=0)
    co_permission = models.BooleanField(default=False)


class LineName(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class AmmoLine(models.Model):
    ammo = models.ForeignKey(Ammo, null=True, on_delete=models.CASCADE)
    linename = models.ForeignKey(LineName, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.ammo.ammo_name+"("+self.linename.name+")"


class Line(models.Model):
    ammoline = models.ForeignKey(
        AmmoLine, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    date_added = models.DateField(null=True)
    lot = models.ForeignKey(Lot, null=True, on_delete=models.CASCADE)


class TurningOver(models.Model):
    lot = models.ManyToManyField(Lot)
    amount = models.IntegerField(null=True)
    ammoline = models.ForeignKey(
        AmmoLine, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True)


# class Leadger(models.Model):
#    issue = models.OneToOneField(Issue, null=True, on_delete=models.CASCADE)
#    line = models.OneToOneField(Line, null=True, on_delete=models.CASCADE)
#    amount = models.IntegerField(null=True)
#    date = models.DateField(null=True)
