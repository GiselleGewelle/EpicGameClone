from django.urls import path
from comment import views

<<<<<<< HEAD

=======
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
urlpatterns = [
    path('', views.CommentCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
]
<<<<<<< HEAD

=======
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
