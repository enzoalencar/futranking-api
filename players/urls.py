from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirectView),
    path('api/players/', views.player_list),
    path('api/players/<int:id>/', views.player_detail),
]