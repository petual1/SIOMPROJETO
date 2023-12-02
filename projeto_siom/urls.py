from django.urls import path
from app_siom import views
from django.contrib import admin  

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('admin/',admin.site.urls),
    path('medicamentos/',views.medicamentos,name='listagem_medicamentos'),
    path('medicamentos/<int:id>',views.receber_compra,name='listagem_medicamentos')
]