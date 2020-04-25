from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_view'),
    path('cat', views.cat_page, name='cat_view')
]