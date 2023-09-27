from django.urls import path
from . import views

urlpatterns = [
    # PUT
    path('total_score/', views.total_score_view, name='total_score_view'), 
    path('target_score/',views.target_score_view,name="target_score_view"),
    path('cost/',views.cost_total_score_view,name="cost_total_score_view"), 

    # GET
    path('score/',views.score_view,name='score_view'), 

    # POST
    path('range/',views.range_view,name="range_view"), 
    path('login/', views.login, name='login'),
    path('todo_item/',views.todo_item_view,name="todo_item_view"),
    # curl --location --request GET '127.0.0.1:8000/entropy_decrease/score/' \
    # --form 'userid="1"'
]
