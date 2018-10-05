from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import geo.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', geo.views.home, name = 'home'),
    path('geoapp/', geo.views.search, name = 'search'),
]
