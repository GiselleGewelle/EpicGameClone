from django.urls import path
from rating import views


urlpatterns = [
    path('', views.MarkCreateView.as_view()),
    path('<int:pk>/', views.MarkDeleteView.as_view()),
]