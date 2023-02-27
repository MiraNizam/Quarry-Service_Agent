from django.contrib import admin
from django.urls import path, include
from datacenter import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.user_orders, name='user_orders'),
    path('profile/', views.user_profile, name='profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('import/', views.import_excel, name='push_excel')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
