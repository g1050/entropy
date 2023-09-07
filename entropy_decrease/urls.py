from django.urls import path
from . import views

urlpatterns = [
    path('my-api/', views.my_custom_view, name='my_custom_view'),
    path('random_num/', views.random_number_view, name='random_number_view'),
    path('test_db/',views.test_db_view,name="test_db_view"),
    path('login/', views.login, name='login'),
]
