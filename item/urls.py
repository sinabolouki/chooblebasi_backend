from django.urls import path
from . import views


urlpatterns = [
    path('item/', views.item_view, name='item_view')
]