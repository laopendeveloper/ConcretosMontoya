"""Tools URLs."""

# Django
from django.urls import path

# Views
from tools import views

urlpatterns = [

    path(
        route='',
        view=views.ToolListView.as_view(),
        name='list'
    ),

    path(
        route='tools/new/',
        view=views.CreateToolView.as_view(),
        name='create'
    ),

    path(
        route='tools/<int:pk>/',
        view=views.ToolDetailView.as_view(),
        name='detail'
    ),

    path(
        route='tools/update/<int:pk>/',
        view=views.UpdateToolView.as_view(),
        name='update'
    ),

]