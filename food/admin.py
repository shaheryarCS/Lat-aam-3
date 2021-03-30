from django.contrib import admin
from .models import Package, Customer, Chef, Appti, Sweet, Main_menu, Order, Price_MainMenu, Price_Apptiti, Price_Sweet, \
    Day_MainMenu, Day_Apptiti, Day_Sweet, Food_Price_Day

# Register your models here.


admin.site.register(Chef)
admin.site.register(Sweet)
admin.site.register(Customer)
admin.site.register(Appti)
admin.site.register(Main_menu)
admin.site.register(Package)
admin.site.register(Order)
admin.site.register(Price_MainMenu)
admin.site.register(Price_Apptiti)
admin.site.register(Price_Sweet)
admin.site.register(Day_Apptiti)
admin.site.register(Day_MainMenu)
admin.site.register(Day_Sweet)
admin.site.register(Food_Price_Day)
