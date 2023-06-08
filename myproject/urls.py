"""myproject URL Configuration

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
from django.urls import path, include, re_path
from myapp.views import (
    register_view, login_view, index,logout_view, members, details, elements, home, testing,template
    )


urlpatterns = [
    path('', index),
    path('login/', login_view),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('myapp.urls')),
]


# Admin Site Config
admin.sites.AdminSite.site_header = 'FERTIGATION SITE ADMINISTRATION'
admin.sites.AdminSite.site_title = 'FERTIGATION PPM PROGRAM'
admin.sites.AdminSite.index_title = 'FERTIGATION ADMIN SITE'