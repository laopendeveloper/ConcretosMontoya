"""Machines URLs."""

# Django
from django.urls import path

# Views
from machines import views

urlpatterns = [

    path(
        route='',
        view=views.MachineListView.as_view(),
        name='feed'
    ),

    path(
        route='machines/new/',
        view=views.CreateMachineView.as_view(),
        name='create'
    ),

    path(
        route='machines/<int:pk>/',
        view=views.MachineDetailView.as_view(),
        name='detail'
    ),

    path(
        route='machines/update/<int:pk>/',
        view=views.UpdateMachineView.as_view(),
        name='update'
    ),

    path(
        route='machines/rent/<int:pk>/',
        view=views.RentMachineView.as_view(),
        name='rent'
    )
]