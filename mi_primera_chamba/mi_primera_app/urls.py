from django.urls import path
from mi_primera_app import views


urlpatterns = [
    path('', views.index),
    path('formpage/', views.form_user_view, name='form_user')
]