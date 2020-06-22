from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category', views.add_category, name='add_category'),
    path('del_category', views.del_category, name='del_category'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
    path('category/<int:category_id>/add_phrase', views.add_phrase, name='add_phrase'),
    path('category/<int:category_id>/del_phrase', views.del_phrase, name='del_phrase'),
]