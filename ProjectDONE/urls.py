"""ProjectDONE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.db import router
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from auction import views



from ProjectDONE import settings
from auction.views import IndexView, SignUpView, AddItemView, LogOutView, LogInView
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'sign_up/', SignUpView.as_view()),
    url(r'additem/', AddItemView.as_view()),
    url(r'logout/', LogOutView.as_view()),
    url(r'signUp/', LogInView.as_view()),
]

# router = routers.DefaultRouter()
# router1.register(r'items', ItemViewAPI)

urlpatterns += [
    # path('', include(router1.urls)),
    path('items/', views.ItemViewAPI.as_view()),
    # path('api/items/<int:pk>/', views.ItemViewAPI.as_view()),
]  # for API view

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)