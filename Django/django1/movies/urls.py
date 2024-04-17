from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.create,name='create'),
    path('edit/<id>',views.edit,name='edit'),
    path('delete/<id>',views.delete,name='delete'),
    path('list/',views.list,name='list'),
    path('',views.index,name='index')
]