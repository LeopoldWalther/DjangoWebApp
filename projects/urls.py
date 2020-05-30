from django.urls import path
 2 from . import views
 3
 4 urlpatterns = [
 5     path("", views.project_index, name="project_index"),
 6     path("<int:pk>/", views.project_detail, name="project_detail"),
 7 ]