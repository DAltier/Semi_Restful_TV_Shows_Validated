from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("shows", views.view_all_shows),
  path("shows/new", views.add_new_show),
  path("shows/create", views.create_new_show),
  path("shows/<int:show_id>", views.view_show),
  path("shows/<int:show_id>/edit", views.edit_show),
  path("shows/<int:show_id>/update", views.update_show),
  path("shows/<int:show_id>/destroy", views.delete_show),
]