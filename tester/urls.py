"""tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from tester_services.views import *
from test_generator.views import *

# for images
from django.conf import settings
from django.conf.urls.static import static

import profiles.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # accounts app
    path('accounts/', include('accounts.urls')),  # signup
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password_change,...

    # profiles app
    path('profile/<int:pk>/', profiles.views.profile, name='profile'),
    path('create_profile/', profiles.views.create_profile, name='create_profile'),
    path('edit_profile/', profiles.views.edit_profile, name='edit_profile'),

    path('my_tests/', my_tests, name='my_tests'),

    # test_generator app
    path('available_tests/', available_tests, name='available_tests'),
    path('create_test/<int:theme>/', create_test, name='create_test'),
    path('generated_test/<int:pk>', generated_test, name='generated_test')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
