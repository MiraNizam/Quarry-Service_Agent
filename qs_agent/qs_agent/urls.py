from django.contrib import admin
from django.urls import path
from datacenter import views


urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('admin/', admin.site.urls),
    path('', views.orders_qs, name='orders'),
]
