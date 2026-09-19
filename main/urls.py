from django.urls import path

from main.views import(

    show_main, show_experience, create_experience, edit_experience, delete_experience,
    show_json_experience, show_json_experience_deserialized,
    show_skill, create_project, show_projects, get_projects_json, delete_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path('skills/', show_skill, name='show_skill'),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/json/", show_json_experience, name="show_json_experience"),
    path("experience/json-deserialized/", show_json_experience_deserialized, name="show_json_experience_deserialized"),
    
]