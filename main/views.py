import json
from django.shortcuts import render, get_object_or_404, redirect, render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse


from main.models import Experience, Skill, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    context = {
        "name": "Geo",
        "fullname": "Georgius Satria Adibrata",
        "npm": "2506589976",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm Geo, a CS Student in Universitas Indonesia."
            "Currently developing my programming skills and I will take any opportunity to improve my abilities!"
        ),
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

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
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
        "name": "Burhan",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
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

    projects_json = serializers.serialize("json", projects)
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
    