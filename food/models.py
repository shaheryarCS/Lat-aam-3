from django.db import models

# Create your models here.
from rest_framework.views import APIView


class Customer(models.Model):
    address = models.CharField(max_length=200,default='SOME STRING')
    name = models.CharField(max_length=100,default='SOME STRING')
    email = models.CharField(max_length=100,default='SOME STRING')
    phoneNo = models.IntegerField(default=0)
    password = models.CharField(max_length=100,default='SOME STRING')




class Chef(models.Model):
    address = models.CharField(max_length=200,default='SOME STRING')
    name = models.CharField(max_length=100,default='SOME STRING')
    email = models.CharField(max_length=100,default='SOME STRING')
    phoneNo = models.IntegerField(default=0)
    password = models.CharField(max_length=100,default='SOME STRING')







class Package(models.Model):
    price = models.IntegerField(default=0)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE,related_name='package_set', null=True, blank=True)
    customer=models.ManyToManyField(Customer, null=True, blank=True)
    package_no=models.IntegerField(default=0)


    @classmethod
    def subscribe(cls,current_cust,new_cust):
        current_cust.customer.add(new_cust)

class Order(models.Model):
    date = models.DateField(auto_now=True)
    customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    Cost=models.IntegerField(default=0)
    time=models.TimeField(auto_now=True)
    packages = models.ForeignKey(Package, on_delete=models.CASCADE)



class Main_menu(models.Model):
    packages = models.ForeignKey(Package, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='SOME STRING')
    price=models.IntegerField(default=0)
    day = models.IntegerField(default=0)


class Sweet(models.Model):
    packages = models.ForeignKey(Package, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='SOME STRING')
    price=models.IntegerField(default=0)
    day = models.IntegerField(default=0)

class Appti(models.Model):
    packages = models.ForeignKey(Package, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='SOME STRING')
    price = models.IntegerField(default=0)
    day = models.IntegerField(default=0)

class Price_MainMenu(models.Model):
    main_menu = models.ForeignKey(Main_menu, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    date=models.DateField(auto_now=True)



class Price_Apptiti(models.Model):
    apptitzer = models.ForeignKey(Appti, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    date=models.DateField(auto_now=True)


class Price_Sweet(models.Model):
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    date=models.DateField(auto_now=True)



class Day_MainMenu(models.Model):
    main_menu = models.ForeignKey(Main_menu, on_delete=models.CASCADE)
    date_No=models.IntegerField(default=0)
    date=models.DateField(auto_now=True)


class Day_Apptiti(models.Model):
    apptitzer = models.ForeignKey(Appti, on_delete=models.CASCADE)
    date_No=models.IntegerField(default=0)
    date=models.DateField(auto_now=True)


class Day_Sweet(models.Model):
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE)
    date_No=models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
##------------------------------------------
class Food_Price_Day(models.Model):
    package=models.IntegerField(default=0)
    foodName=models.CharField(max_length=100,default='SOME STRING')
    chef=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    day=models.IntegerField(default=0)
    foodType = models.CharField(max_length=100, default='SOME STRING')



##----------https://github.com/aarav-tech/ems/blob/master/poll/models.py-------------------------------------------------------

##    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Question(models.Model):
    title = models.TextField(null=False, blank=False)
    status = models.CharField(default='inactive', max_length=10)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()





class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __unicode__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()