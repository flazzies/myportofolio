import json
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini


from main.models import Experience, Skill, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')

    context = {
        "name": "Geo",
        "fullname": "Georgius Satria Adibrata",
        "npm": "2506589976",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm Geo, a CS Student in Universitas Indonesia."
            "Currently developing my programming skills and I will take any opportunity to improve my abilities!"
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)




def show_skill(request):
    category_filter = request.GET.get('category')
    proficiency_filter = request.GET.get('proficiency')
    
    skills = Skill.objects.all()
    
    if category_filter:
        skills = Skill.objects.filter(category=category_filter)

    if proficiency_filter:
        skills = Skill.objects.filter(proficiency=proficiency_filter)

    
    context = {
        "name": "Geo",
        "fullname" : "Georgius Satria Adibrata",
        "skill_list": skills,
    }
    return render(request, "skills.html", context)

@login_required(login_url="/login/") 
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Geo",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Geo",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/") 
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True  # Tambahkan argumen ini
    )
    return HttpResponse(projects_json, content_type="application/json")

def show_experience(request):
    context = {
        "name": "Geo",
        "fullname" : "Georgius Satria Adibrata",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method=="POST":
        form.save()
        messages.success(request, 'Pengalaman berhasil ditambahkan!')
        return redirect('main:show_experience')
    context = {
        "name": "Geo",
        "fullname": "Georgius Satria Adibrata",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        messages.info(request, 'Pengalaman berhasil diperbarui!')
        return redirect('main:show_experience')
    
    context = {
        "name": "Geo",
        "fullname": "Georgius Satria Adibrata",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    messages.warning(request, 'Pengalaman berhasil dihapus!')
    return redirect('main:show_experience')

def show_json_experience(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_experience_deserialized(request):
    data_json = serializers.serialize("json", Experience.objects.all())
    deserialized_objects = [obj.object for obj in serializers.deserialize("json", data_json)]
    
    context = {
        "name": "Geo",
        "fullname": "Georgius Satria Adibrata",
        "experience_list": deserialized_objects,
    }
    return render(request, 'experience.html', context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Geo",
        "form": form,
    }
    return render(request, "register.html", context)    


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Geo",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")