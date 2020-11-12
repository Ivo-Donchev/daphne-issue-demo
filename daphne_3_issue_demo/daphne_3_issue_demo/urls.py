from django.contrib import admin
from django.urls import path
from .views import view_1, view_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', view_1),
    path('2/', view_2),
]
