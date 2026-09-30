from django.urls import path

from main.views import(

    show_main, show_experience, create_experience, edit_experience, delete_experience,
    show_json_experience, show_json_experience_deserialized,
    show_skill, create_project, show_projects, get_projects_json, delete_project,
    register, login_user, logout_user, toggle_star, toggle_endorse,
    create_project_ajax, toggle_star_experience, create_experience_ajax
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
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/",toggle_star,name="toggle_star",),
    path('skills/<uuid:skill_id>/endorse/', toggle_endorse, name='toggle_endorse'),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    # Tambahkan path ini ke dalam urlpatterns
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience",),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),

    
]