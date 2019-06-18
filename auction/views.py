from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


#from .serializers import ItemSerializer
#from rest_framework import viewsets, mixins, generics

from auction.models import Item, Photo


class IndexView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request,
                      'index.html',
                      {'items': items})


class SignUpView(View):
    def get(self, request):
        logout(request)
        return render(request,
                      'register.html')

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['email'],
                                            password=request.POST['password1'])
            #login(request, user)
            return redirect('/')
        else:
            return render(request,
                      'register.html', {'error': 'Passwords are not '
                                                     'equal'})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')


class LogInView(View):
    def get(self, request):
        return render(request,
                      'signUp.html')

    def post(self, request):
        userlog = authenticate(username=request.POST['email'], password=request.POST['password1'])
        if userlog is not None:
            login(request, userlog)
            return (redirect('/'))
        else:
            return render(request,
                          'signUp.html', {'error': 'no USER found!'})


class AddItemView(View):
    def get(self, request):
        return render(request,
                      'additem.html')

    def post(self, request):
        photo = Photo.objects.create(photo=request.FILES['photo'])
        #print(photo)
        item = Item.objects.create(name=request.POST['nameI'],
                                    date_stop=request.POST['dateS'],
                                    description=request.POST['description'],
                                   price=request.POST['price'],
                                   photo=photo
                                   )
        return redirect('/')


# class ItemViewAPI(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)