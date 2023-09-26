# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('calculate/<int:a>/<int:b>/', views.calculate_sum, name='calculate_sum'),
    path('check_result/<str:task_id>', views.check_result, name='check_result'),
    path('input/', views.NumbersInputView.as_view(), name='numbers_input'),
    path('check_result_of_a_queue/<str:queue_name>', views.check_result_of_a_queue, name='check_result_of_a_queue'),

]
