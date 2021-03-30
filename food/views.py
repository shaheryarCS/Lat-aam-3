
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, status
from .models import Package, Customer, Chef, Appti, Sweet, Main_menu, Order, Price_MainMenu, Price_Apptiti, Price_Sweet, \
    Day_MainMenu, Day_Apptiti, Day_Sweet, Food_Price_Day, Question, Choice, Musician
from .serializers import chefSerializer, Main_menu_Serializer, chefUpdateAndDelete, Appti_Serializer, \
    Customer_Serializer, Package_Serializer, Sweet_Serializer, chefRegisterSerializer, chefLoginSerializer, \
    Price_MainMenu_Serializer, Price_Sweet_Serializer, Day_MainMenu_Serializer, Day_Apptiti_Serializer, \
    Day_Sweet_Serializer, FoofRegisterSerializer, menuSerializer2, QuestionSerializer, ChoiceSerializer, \
    chef_package_Serializer, MusicianSerializer, Order_Serializer

from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework import permissions as rest_permissions

class cheflist(APIView):

    def get(self,request):
        book1 = Chef.objects.all()
        serializer = chefSerializer(book1, many= True)
        return Response(serializer.data) # Return JSON



class chefName(generics.ListCreateAPIView): ##  useful for "one" item
        search_fields = ['password']
        filter_backends=(filters.SearchFilter,)
        queryset = Chef.objects.all()
        serializer_class = chefSerializer


class chefDetail(generics.RetrieveUpdateDestroyAPIView): ## it is not useful
    queryset = Chef.objects.all()
    serializer_class = chefSerializer


class chefCRUD(generics.ListCreateAPIView): ##  useful for posting one chef
##class chefCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = chefSerializer


class chefUpdateView(generics.UpdateAPIView): ## useful for update chef with given ID
    queryset = Chef.objects.all()
    serializer_class = chefSerializer


class chefDeleteView(generics.DestroyAPIView):## useful for delete chef with given ID
    queryset = Chef.objects.all()
    serializer_class = chefSerializer



class ChefGet(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['password', ]
    filter_backends = (filters.SearchFilter,)
    queryset = Chef.objects.all()
    serializer_class = chefSerializer


##------------------------Order API functions---------------
class orderCRUD(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = Order_Serializer


class orderUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Order.objects.all()
    serializer_class = Order_Serializer


class orderDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Order.objects.all()
    serializer_class = Order_Serializer

class orderGet(generics.ListCreateAPIView):  ##  useful for "one" item
        # search_fields = ['packages__id','date']
        search_fields = ['chef__id',]
        filter_backends = (filters.SearchFilter,)
        queryset = Order.objects.all()
        serializer_class = Order_Serializer



class orderlist(APIView):

    def get(self,request):
        book1 = Order.objects.all()
        serializer = Order_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON





##------------------------Main_menu API functions---------------
class Main_menuCRUD(generics.ListCreateAPIView):
    queryset = Main_menu.objects.all()
    serializer_class = Main_menu_Serializer


class Main_menuUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Main_menu.objects.all()
    serializer_class = Main_menu_Serializer


class Main_menuDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Main_menu.objects.all()
    serializer_class = Main_menu_Serializer

class Main_menuGet(generics.ListCreateAPIView):  ##  useful for "one" item
        search_fields = ['chef__id',]
        filter_backends = (filters.SearchFilter,)
        queryset = Main_menu.objects.all()
        serializer_class = Main_menu_Serializer



class MainMenulist(APIView):

    def get(self,request):
        book1 = Main_menu.objects.all()
        serializer = Main_menu_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON




##------------------------Appiti API functions---------------
class Appti_CRUD(generics.ListCreateAPIView):
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer


class ApptiUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer


class ApptiDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer

class ApptiGet(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['chef__id', ]
    filter_backends = (filters.SearchFilter,)
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer



class Apptilist(APIView):

    def get(self,request):
        book1 = Appti.objects.all()
        serializer = Appti_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON



##------------------------Sweet API functions---------------
class Sweet_CRUD(generics.ListCreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = Sweet_Serializer


class SweetUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Sweet.objects.all()
    serializer_class = Sweet_Serializer


class SweetDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Sweet.objects.all()
    serializer_class = Sweet_Serializer

class SweetGet(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['chef__id',]
    filter_backends = (filters.SearchFilter,)
    queryset = Sweet.objects.all()
    serializer_class = Sweet_Serializer



class Sweetlist(APIView):

    def get(self,request):
        book1 = Sweet.objects.all()
        serializer = Sweet_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON




##------------------------Package API functions---------------
class Package_CRUD(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = Package_Serializer


class PackageUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Package.objects.all()
    serializer_class = Package_Serializer


class PackageDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Package.objects.all()
    serializer_class = Package_Serializer

class PackageGet(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['chef__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Package.objects.all()
    serializer_class = Package_Serializer

class PackageGetById(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Package.objects.all()
    serializer_class = Package_Serializer




class Packagelist(APIView):

    def get(self,request):
        book1 = Package.objects.all()
        serializer = Package_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON


def change_cust(request,instruction,pk):
    pack=Package.objects.get(pk=pk)
    if instruction=='subscribe':
        Package.subscribe(request.cust,pack)




##------------------------Customer API functions---------------
class Customer_CRUD(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer


class CustomerUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer


class CustomerDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer





class Customerlist(APIView):

    def get(self,request):
        book1 = Customer.objects.all()
        serializer = Customer_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON

class CustomerGet(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['password', ]
    filter_backends = (filters.SearchFilter,)
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer

class CustomerGetByID(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['id', ]
    filter_backends = (filters.SearchFilter,)
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer



class register_chef_view(CreateAPIView):  ## useful for sign in chef
    queryset = Chef.objects.all()
    serializer_class = chefRegisterSerializer


class login_chef_view(RetrieveAPIView):  ## useful for login
    queryset = Chef.objects.all()
    serializer_class = chefLoginSerializer




class OrderListDate(generics.ListAPIView):
    serializer_class =Order_Serializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        param1 = self.request.GET['param1']
        param2 = self.request.GET['param2']
        user = self.request.user
        # return Order.objects.filter(date__range=["2011-01-01", "2011-01-31"])
        return Order.objects.filter(date__range=[param1, param2])

class OrderListDate2(APIView):

    def get(self,request,param1,param2):
        # book1 = Order.objects.filter(date__range=[param1, param2])
        book1 = Order.objects.filter(Cost=param1)
        serializer = Order_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON
#
#
# def OrderListDate2(request, param1, param2):
#
#         # return Order.objects.filter(date__range=["2011-01-01", "2011-01-31"])
#         return Order.objects.filter(date__range=[param1, param2])
class OrderListDate3(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['date']
    filter_backends = (filters.SearchFilter,)
    queryset = Price_MainMenu.objects.all()
    serializer_class = Price_MainMenu_Serializer

##------------------------Price_MainMenu API functions---------------
class Price_MainMenu_CRUD(generics.ListCreateAPIView):
    queryset = Price_MainMenu.objects.all()
    serializer_class = Price_MainMenu_Serializer


class Price_MainMenuUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Price_MainMenu.objects.all()
    serializer_class = Price_MainMenu_Serializer


class Price_MainMenuDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Price_MainMenu.objects.all()
    serializer_class = Price_MainMenu_Serializer

class Price_MainMenuGet(generics.ListCreateAPIView):  ##  useful for "one" item
    search_fields = ['price']
    filter_backends = (filters.SearchFilter,)
    queryset = Price_MainMenu.objects.all()
    serializer_class = Price_MainMenu_Serializer


class Price_MainMenulist(APIView):

    def get(self,request):
        book1 = Price_MainMenu.objects.all()
        serializer = Price_MainMenu_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON





##------------------------Price_Sweet API functions---------------
class Price_Sweet_CRUD(generics.ListCreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = Price_Sweet_Serializer


class Price_SweetUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Sweet.objects.all()
    serializer_class = Price_Sweet_Serializer


class Price_SweetDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Sweet.objects.all()
    serializer_class = Price_Sweet_Serializer

    class Price_SweetGet(generics.ListCreateAPIView):  ##  useful for "one" item
        search_fields = ['price']
        filter_backends = (filters.SearchFilter,)
        queryset = Sweet.objects.all()
        serializer_class = Price_Sweet_Serializer




class Price_Sweetilist(APIView):

    def get(self,request):
        book1 = Sweet.objects.all()
        serializer = Price_Sweet_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON





##------------------------Price_Appiti API functions---------------
class Price_Appti_CRUD(generics.ListCreateAPIView):
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer


class Price_ApptiUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer


class Price_ApptiDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Appti.objects.all()
    serializer_class = Appti_Serializer

class Price_ApptiGet(generics.ListCreateAPIView):  ##  useful for "one" item
        search_fields = ['price']
        filter_backends = (filters.SearchFilter,)
        queryset = Appti.objects.all()
        serializer_class = Appti_Serializer




class Price_Apptilist(APIView):

    def get(self,request):
        book1 = Appti.objects.all()
        serializer = Appti_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON






##------------------------Day_MainMenu API functions---------------
class Day_MainMenu_CRUD(generics.ListCreateAPIView):
    queryset = Day_MainMenu.objects.all()
    serializer_class = Day_MainMenu_Serializer


class Day_MainMenuUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Day_MainMenu.objects.all()
    serializer_class = Day_MainMenu_Serializer


class Day_MainMenuDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Day_MainMenu.objects.all()
    serializer_class = Day_MainMenu_Serializer

class Day_MainMenuGet(generics.ListCreateAPIView):  ##  useful for "one" item
        search_fields = ['main_menu__id']
        filter_backends = (filters.SearchFilter,)
        queryset = Day_MainMenu.objects.all()
        serializer_class = Day_MainMenu_Serializer




class Day_MainMenulist(APIView):

    def get(self,request):
        book1 = Day_MainMenu.objects.all()
        serializer = Day_MainMenu_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON





##------------------------Day_Appiti API functions---------------
class Day_Apptiti_CRUD(generics.ListCreateAPIView):
    queryset = Day_Apptiti.objects.all()
    serializer_class = Day_Apptiti_Serializer


class Day_ApptitiUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Day_Apptiti.objects.all()
    serializer_class = Day_Apptiti_Serializer


class Day_ApptitiDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Day_Apptiti.objects.all()
    serializer_class = Day_Apptiti_Serializer

class Day_ApptitiGet(generics.ListCreateAPIView):  ##  useful for "one" item
        search_fields = ['apptitzer__id']
        filter_backends = (filters.SearchFilter,)
        queryset = Day_Apptiti.objects.all()
        serializer_class = Day_Apptiti_Serializer


class Day_Apptitilist(APIView):

    def get(self,request):
        book1 = Day_Apptiti.objects.all()
        serializer = Day_Apptiti_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON





##------------------------Day_Sweet API functions---------------
class Day_Sweet_CRUD(generics.ListCreateAPIView):
    queryset = Day_Sweet.objects.all()
    serializer_class = Day_Sweet_Serializer


class Day_SweetUpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Day_Sweet.objects.all()
    serializer_class = Day_Sweet_Serializer


class Day_SweetDeleteView(generics.DestroyAPIView):  ## useful for delete chef with given ID
    queryset = Day_Sweet.objects.all()
    serializer_class = Day_Sweet_Serializer

class Day_SweetGet(generics.ListCreateAPIView):  ##  useful for "one" item
        search_fields = ['sweet__id']
        filter_backends = (filters.SearchFilter,)
        queryset = Day_Sweet.objects.all()
        serializer_class = Day_Sweet_Serializer


class Day_Sweetlist(APIView):

    def get(self,request):
        book1 = Day_Sweet.objects.all()
        serializer = Day_Sweet_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON

##-----------------------Food_Price_Day---------------------

class Food_Price_Day_CRUD(CreateAPIView):
    queryset = Food_Price_Day.objects.all()
    serializer_class = FoofRegisterSerializer



class foodView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = menuSerializer2(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            serializer = menuSerializer2(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



##-------------------------------------------------

class Ques_CRUD(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class Choi_CRUD(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class chef_Pack_CRUD(generics.ListCreateAPIView): ##  useful for posting one chef
##class chefCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = chef_package_Serializer





class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer



class chef_Pack_List(APIView):

    def get(self,request):
        book1 = chef_Pack_CRUD.objects.all()
        serializer = chef_package_Serializer(book1, many= True)
        return Response(serializer.data) # Return JSON


class chef_Pack_RUD(generics.UpdateAPIView):
    serializer_class = chef_package_Serializer
    queryset = Package.objects.all()


class Packae_UpdateView(generics.UpdateAPIView):  ## useful for update chef with given ID
    queryset = Package.objects.all()
    serializer_class = Package_Serializer