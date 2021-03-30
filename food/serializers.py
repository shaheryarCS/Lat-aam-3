import sys

from rest_framework import serializers, fields
from .models import Chef, Main_menu, Appti, Sweet, Package, Customer, Price_MainMenu, Price_Apptiti, \
    Price_Sweet, Day_MainMenu, Day_Apptiti, Day_Sweet, Food_Price_Day, Question, Choice, Album, Musician, \
    Order  # import model

from rest_framework.serializers import (ValidationError)

# Create a class
class chefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chef
        fields = '__all__'


class chefRegisterSerializer(serializers.ModelSerializer): ## sign-in

    class Meta:
        model = Chef
        fields = '__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, data):
        email=data['email']
        chef_qs= Chef.objects.filter(email=email)
        if chef_qs.exists():
            raise  ValidationError("false")
        return  data


    def create(self, validated_data):
        name=validated_data['name']
        password = validated_data['password']
        email = validated_data['email']
        phoneNo = validated_data['phoneNo']
        address = validated_data['address']
        chef_obj=Chef(
            name=name,
            password=password+name,
            email=email,
        phoneNo = phoneNo,
        address = address
        )

       ## chef_obj.set_password(password)
        chef_obj.save()
        return  validated_data



class customerRegisterSerializer(serializers.ModelSerializer): ## sign-in

    class Meta:
        model = Chef
        fields = '__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, data):
        email=data['email']
        chef_qs= Chef.objects.filter(email=email)
        if chef_qs.exists():
            raise  ValidationError("false")
        return  data


    def create(self, validated_data):
        name=validated_data['name']
        password = validated_data['password']
        email = validated_data['email']
        phoneNo = validated_data['phoneNo']
        address = validated_data['address']
        chef_obj=Chef(
            name=name,
            password=password+name,
            email=email,
        phoneNo = phoneNo,
        address = address
        )

       ## chef_obj.set_password(password)
        chef_obj.save()
        return  validated_data







class chefLoginSerializer(serializers.ModelSerializer): ## sign-in

    class Meta:
        model = Chef
        fields = '__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, data):
        username = data.get("name",None)
        password = data.get("password", None)

        if not username and not password:
            raise  ValidationError("A username or password required")

        user= Chef.objects.get(password__exact=password)

        if user.exists():
            username="a"
        else:
            raise ValidationError("Incorrect password or username")
        return data

class chefUpdateAndDelete(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.aphoneNo = validated_data.get('phoneNo', instance.phoneNo)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance


class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class Main_menu_Serializer(serializers.ModelSerializer):



    class Meta:
        model = Main_menu
        fields = '__all__'



class Appti_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Appti
        fields = '__all__'



class Sweet_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Sweet
        fields = '__all__'





class Package_Serializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = Package
        fields = '__all__'



class chef_package_Serializer(serializers.ModelSerializer):
    package_set = Package_Serializer(many=True)
    class Meta:
        model = Chef
        fields = ('address', 'name', 'email', 'phoneNo', 'password', 'package_set')
       ## fields = '__all__'

    def create(self, validated_data):
        package_data = validated_data.pop('package_set')
        musician = Chef.objects.create(**validated_data)
        for album_data in package_data:
            Package.objects.create(chef=musician, **album_data)
        return musician


    def update(self, instance, validated_data):
        package_data = validated_data.pop('package_set')
        packages = (instance.package_set).all()
        packages = list(packages)
        instance.address = validated_data.get('address', instance.address)
        instance.name = validated_data.get('name', instance.name)
        instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        for album_data in package_data:
            album = packages.pop(0)
            album.price = album_data.get('price', album.price)
            album.package_no = album_data.get('package_no', album.package_no)
            album.save()
        return instance




class Customer_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'



class Customer_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class Price_MainMenu_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Price_MainMenu
        fields = '__all__'


class Price_Apptiti_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Price_Apptiti
        fields = '__all__'


class Price_Sweet_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Price_Sweet
        fields = '__all__'


class Day_MainMenu_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Day_MainMenu
        fields = '__all__'


class Day_Apptiti_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Day_Apptiti
        fields = '__all__'


class Day_Sweet_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Day_Sweet
        fields = '__all__'



class Day_Sweet_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Day_Sweet
        fields = '__all__'

##----------------------------------------------





class FoofRegisterSerializer(serializers.ModelSerializer): ## sign-in

    class Meta:
        model = Food_Price_Day
        fields = '__all__'
        #
        # extra_kwargs={
        #     'price':{'write_only':True}
        # }

    #
    # def validate(self, data):
    #     email=data['price']
    #     chef_qs= Food_Price_Day.objects.filter(price=email)
    #     if chef_qs.exists():
    #          raise  ValidationError("This user has already registered")
    #     return  data

    def create(self, validated_data):

        try:
            package = validated_data['package']
            foodName = validated_data['foodName']
            chef = validated_data['chef']
            price = validated_data['price']
            day = validated_data['day']
            foodType = validated_data['foodType']
            #
            # obj_food=""
            # obj_price="";
            # obj_day="";
            # obj_food = Food_Price_Day(package=2
            #                      , foodName="foodName"
            #                      , chef=2,
            #                      price=89,
            #                      day=1,
            #                      foodType="foodType")
            # obj_food.save()
            #
            #
            #
            # if(validated_data['food_Type']=="M"):
            #     obj_food = Main_menu( package=2,chef=chef, name=food_name)
            #     obj_food.save()
            #     obj_price = Price_MainMenu(main_menu=obj_food.id , price=chef)
            #     obj_price.save()
            #     obj_day = Day_MainMenu(main_menu=obj_food.id, date_No=day)
            #     obj_day.save()
            #
            #
            # if(validated_data['food_Type']=="A"):
            #     obj_food = Appti(package=package, chef=chef, name=food_name)
            #     obj_food.save()
            #     obj_price = Price_Apptiti(main_menu=obj_food.id, price=chef)
            #     obj_price.save()
            #     obj_day = Day_Apptiti(main_menu=obj_food.id, date_No=day)
            #     obj_day.save()
            #
            #
            # if(validated_data['food_Type']=="S"):
            #     obj_food = Sweet(package=package, chef=chef, name=food_name)
            #     obj_food.save()
            #     obj_price = Price_Sweet(main_menu=obj_food.id, price=chef)
            #     obj_price.save()
            #     obj_day = Day_Sweet(main_menu=obj_food.id, date_No=day)
            #     obj_day.save()
            question = Food_Price_Day.objects.create(**validated_data)

            return validated_data
        except:
            # Prints the error and the line that causes the error
            print("%s - %s at line: %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))




class main2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Day_MainMenu
        fields = ('date_No',)

class menuSerializer2(serializers.ModelSerializer): ## sign-in

    day_set=main2Serializer(many=True)
    class Meta:
        model = Main_menu
       # fields = '__all__'
        fields=('packages','chef','name','day_set')

        def create(self, validated_data):
            day_validated_data = validated_data.pop('day_set')
            food = Main_menu.objects.create(**validated_data)
            day_set_serializer = self.fields['day_set']

            for each in day_validated_data:
                each['food'] = food
            day = main2Serializer.create(day_validated_data)

            return food





##-----------------------https://github.com/aarav-tech/ems/blob/master/poll/serializers.py------------------------



class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Choice
        fields = [
            'id',
            'question',
            'text'
        ]
        read_only_fields = ('question',)




class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "title",
            "status",
            "choices",
        ]

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(**choice, question=question)
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    c = Choice.objects.get(id=choice["id"])
                    c.text = choice.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance







class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars')


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')

    def create(self, validated_data):
        albums_data = validated_data.pop('album_musician')
        musician = Musician.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=musician, **album_data)
        return musician