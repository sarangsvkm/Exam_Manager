from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('add/', views.add_exam, name='add_exam'),
     path('update/<int:id>/', views.update_exam, name='update_exam')
]
