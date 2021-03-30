from django.urls import path

from . import views

app_name = 'food'


urlpatterns = [
    path('chefs/', views.cheflist.as_view()),
    path('chefs/<int:pk>', views.chefUpdateView.as_view()), ## it is uesd for "updating" the chef in Database
    path('chefDeletes/<int:pk>', views.chefDeleteView.as_view()), ## it is uesd for "deleting" the chef in Database
    path('chefName/', views.chefName.as_view()),
    path('chefDetail/<int:pk>/', views.chefDetail.as_view()),
    path('chefCRUD/', views.chefCRUD.as_view()), ## it is uesd for "posting" the chef in Database
    ##path('chefCRUD/<int:pk>/', views.chefCRUD.as_view()),
    path('Main_menuCRUD/', views.Main_menuCRUD.as_view()),
    path('register_chef_view/', views.register_chef_view.as_view()),
    path('login_chef_view/', views.login_chef_view.as_view()),
    path('ChefGet/', views.ChefGet.as_view()),


##---------------Order URLS----------------------------
    path('orderUpdateView/<int:pk>', views.orderUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('orderDeleteView/<int:pk>', views.orderDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('orderCRUD/', views.orderCRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('orderlist/', views.orderlist.as_view()),  ## it is uesd for "posting" the chef in Database
    path('orderGet/', views.orderGet.as_view()),  ## it is uesd for "posting" the chef in Database
    path('OrderListDate/$', views.OrderListDate.as_view()),
    path('OrderListDate2/(?P<param1>[\w-]+)/(?P<param2>[\w-]+)/$', views.OrderListDate2.as_view()),
    path('OrderListDate3/', views.OrderListDate3.as_view()),

    ##---------------Main_menu URLS----------------------------
    path('mainMenuUpdate/<int:pk>', views.Main_menuUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('mainMenuDeletes/<int:pk>', views.Main_menuDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('mainMenuCRUD/', views.Main_menuCRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('MainMenulist/', views.MainMenulist.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Main_menuGet/', views.Main_menuGet.as_view()),  ## it is uesd for "posting" the chef in Database

    ##---------------Appiti URLS----------------------------
    path('appitiUpdate/<int:pk>', views.ApptiUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('appitiDeletes/<int:pk>', views.ApptiDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('appitiCRUD/', views.Appti_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('ApptiGet/', views.ApptiGet.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Apptilist/', views.ApptiGet.as_view()),  ## it is uesd for "posting" the chef in Database

    ##---------------Sweet URLS----------------------------
    path('sweetUpdate/<int:pk>', views.SweetUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('sweetDeletes/<int:pk>', views.SweetDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('sweetCRUD/', views.Sweet_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('SweetGet/', views.SweetGet.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Sweetlist/', views.SweetGet.as_view()),  ## it is uesd for "posting" the chef in Database

    ##---------------Package URLS----------------------------
    path('packageUpdate/<int:pk>', views.PackageUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('packageDeletes/<int:pk>', views.PackageDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('packageCRUD/', views.Package_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Packagelist/', views.Packagelist.as_view()),
    path('PackageGet/', views.PackageGet.as_view()),
    path('PackageCustAdd/<instruction>/<pk>', views.change_cust),
    path('PackageGetById/', views.PackageGetById.as_view()),

    ##---------------Customer URLS----------------------------
    path('customerUpdate/<int:pk>', views.CustomerUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('customerDeletes/<int:pk>', views.CustomerDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('customerCRUD/', views.Customer_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Customerlist/', views.Customerlist.as_view()),
    path('CustomerGet/', views.CustomerGet.as_view()),
    path('CustomerGetByID/', views.CustomerGetByID.as_view()),

##---------------Price Main menu URLS----------------------------
    path('Price_MainMenuUpdateView/<int:pk>', views.Price_MainMenuUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('Price_MainMenuDeleteView/<int:pk>', views.Price_MainMenuDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('Price_MainMenu_CRUD/', views.Price_MainMenu_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database




##---------------Price Appiti URLS----------------------------
    path('Price_ApptiUpdateView/<int:pk>', views.Price_ApptiUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('Price_ApptiDeleteView/<int:pk>', views.Price_MainMenuDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('Price_Appti_CRUD/', views.Price_Appti_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database



##---------------Price Sweet URLS----------------------------
    path('Price_SweetUpdateView/<int:pk>', views.Price_SweetUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('Price_SweetDeleteView/<int:pk>', views.Price_SweetDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('Price_Sweet_CRUD/', views.Price_Sweet_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database


##---------------Day Main menu URLS----------------------------
    path('Day_MainMenuUpdateView/<int:pk>', views.Day_MainMenuUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('Day_MainMenuDeleteView/<int:pk>', views.Day_MainMenuDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('Day_MainMenu_CRUD/', views.Day_MainMenu_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Day_MainMenulist/', views.Day_MainMenulist.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Day_MainMenuGet/', views.Day_MainMenuGet.as_view()),  ## it is uesd for "posting" the chef in Database

##---------------Day Appiti URLS----------------------------
    path('Day_ApptitiUpdateView/<int:pk>', views.Day_ApptitiUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('Day_ApptitiDeleteView/<int:pk>', views.Day_ApptitiDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('Day_Apptiti_CRUD/', views.Day_Apptiti_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Day_Apptitilist/', views.Day_Apptitilist.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Day_ApptitiGet/', views.Day_ApptitiGet.as_view()),  ## it is uesd for "posting" the chef in Database





##---------------Day Sweet URLS----------------------------
    path('Day_SweetUpdateView/<int:pk>', views.Day_SweetUpdateView.as_view()),  ## it is uesd for "updating" the chef in Database
    path('Day_SweetDeleteView/<int:pk>', views.Day_SweetDeleteView.as_view()),  ## it is uesd for "deleting" the chef in Database
    path('Day_Sweet_CRUD/', views.Day_Sweet_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Day_Sweetlist/', views.Day_Sweetlist.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Day_SweetGet/', views.Day_SweetGet.as_view()),  ## it is uesd for "posting" the chef in Database


    ##-----------------------Food_Price_Day----------------

    path('Food_Price_Day/', views.Food_Price_Day_CRUD.as_view()),  ## it is uesd for "posting" the chef in Database
    path('Foodpost/', views.foodView.as_view()),


path('Ques_CRUD/', views.Ques_CRUD.as_view()),

path('Choi_CRUD/', views.Choi_CRUD.as_view()),


path('chef_Pack_CRUD/', views.chef_Pack_CRUD.as_view()),

path('chef_Pack_List/', views.cheflist.as_view()),


path('chef_Pack_RUD/<int:pk>', views.chef_Pack_RUD.as_view()),



path('Packae_UpdateView/<int:pk>', views.Packae_UpdateView.as_view()),

path('MusicianListView/', views.MusicianListView.as_view()),

# url(r'^api/musicians/$', MusicianListView.as_view()),
]