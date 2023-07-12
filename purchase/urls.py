from django.urls import path
from order import views


urlpatterns = [
    path('', views.PurchaseCreateView.as_view()),
    path('<int:pk>/', views.PurchaseCreateView.as_view()),
]