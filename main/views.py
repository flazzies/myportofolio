from django.shortcuts import render

from main.models import Experience, Skill

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


def show_experience(request):
    context = {
        "name": "Geo",
        "fullname" : "Georgius Satria Adibrata",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skill(request):
    context = {
        "name": "Geo",
        "fullname" : "Georgius Satria Adibrata",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skills.html", context)