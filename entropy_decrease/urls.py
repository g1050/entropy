from django.urls import path
from . import views

urlpatterns = [
    path('total_score/', views.total_score_view, name='total_score_view'), # PUT
    path('target_score',views.target_score_view,name="target_score_view"), # PUT
    path('login/', views.login, name='login'), # POST
    path('score/',views.score_view,name='score_view'), # GET
    path('cost/',views.cost_total_score_view,name="cost_total_score_view") # PUT
]
