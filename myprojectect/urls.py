from playground import views
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('webhook',views.webhook,name='webhook'),
    path('accounts/', include('allauth.urls')),
    path('homes/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('home/', views.home),
]
