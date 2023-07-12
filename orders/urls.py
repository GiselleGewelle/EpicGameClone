from django.urls import path
from order import views


urlpatterns = [
    path('', views.OrderCreateView.as_view()),
    path('<int:pk>/', views.OrderCreateView.as_view()),
]