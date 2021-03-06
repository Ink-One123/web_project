"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('test/', include('test.urls')),
    # 다음과 같이 정의하면 장고는 test/ 로 들어오는 모든 요청을 test.urls로 전송하여 탐색한다.
    # urls파일을 분리할때 사용할 수 있는 기능이다.
    
    path('admin/', admin.site.urls),

    path('', views.main, name='main'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    

    # path('idfound/', views.login, name='idfound'),
    # path('passwordfound/', views.login, name='passwordfound'),

    path('mypage/', views.mypage, name='mypage'),

    # path('/studyroom', views.login, name='studyroom'),
]
