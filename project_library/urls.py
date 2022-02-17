from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('library.urls')),
    path("api/", include("api.urls")),
    path('admin/', admin.site.urls),
]
