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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from myapp.views import (
    register_view, login_view, index,logout_view, dashboard, Fertilizers, elements, home, testing,template
    )


urlpatterns = [
    path('', login_view),
    path('logout/', logout_view),
    path('admin/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('myapp.urls')),
    path('images/', include('myapp.urls')),
]


# Serving media files during development (Not recommended for production)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Site Config
admin.sites.AdminSite.site_header = 'FERTIGATION SITE ADMINISTRATION'
admin.sites.AdminSite.site_title = 'FERTIGATION PPM PROGRAM'
admin.sites.AdminSite.index_title = 'FERTIGATION ADMIN SITE'
