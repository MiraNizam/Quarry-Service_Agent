from django.contrib import admin
from django.urls import path, include
from datacenter import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.user_orders, name='user_orders'),
    path('profile/', views.user_profile, name='profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
