
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('complist/', include('complist.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('competitions/', include('competitions.urls')),
]
