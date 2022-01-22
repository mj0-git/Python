from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from autos.views import MainView

app_name = 'autos'

urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]