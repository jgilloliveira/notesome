"""api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

LIST_CREATE_VIEW_ARGS = {'post':'create', 'get':'list'}
BY_ID_VIEW_ARGS = {'get':'retrieve', 'put':'partial_update', 'delete':'destroy'}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', include('apps.categories.urls')),
    path('api/folders/', include('apps.folders.urls')),
    path('api/notes/', include('apps.notes.urls')),
    path('api/users/', include('apps.users.urls')),
]
