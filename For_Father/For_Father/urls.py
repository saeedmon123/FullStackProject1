from django.contrib import admin
from django.urls import path
from father.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Attach the NinjaAPI instance here
]
