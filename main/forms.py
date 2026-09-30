from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateField, DateInput

from main.models import Project, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [  
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
        
class ExperienceForm(ModelForm):
    started_at = DateField(
        label="Tanggal Mulai",
        widget=DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']
    )
    ended_at = DateField(
        label="Tanggal Selesai",
        required=False, # Opsional jika masih berlangsung
        widget=DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']
    )

    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail", "started_at", "ended_at"]
        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Logo / Gambar",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan peran dan pencapaianmu",
                    "rows": 3,
                }
            ),
            "category": Select(attrs={
                'class': 'custom-select',
            }),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/logo.png",
                }
            )
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data.get("title", "")).strip()
        if not title:
            raise ValidationError("Nama pengalaman tidak boleh kosong atau hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data.get("description", "")).strip()
        if not description:
            raise ValidationError("Deskripsi tidak boleh kosong atau hanya berisi tag HTML.")
        return description

    def clean_category(self):
        category = strip_tags(self.cleaned_data.get("category", "")).strip()
        if not category:
            raise ValidationError("Kategori tidak boleh kosong.")
        return category

    def clean_thumbnail(self):
        thumbnail = strip_tags(self.cleaned_data.get("thumbnail", "")).strip()
        return thumbnail

    # Validasi Silang (membandingkan started_at dan ended_at)
    def clean(self):
        cleaned_data = super().clean()
        started_at = cleaned_data.get("started_at")
        ended_at = cleaned_data.get("ended_at")

        if started_at and ended_at and ended_at < started_at:
            self.add_error('ended_at', "Tanggal selesai tidak boleh lebih awal dari tanggal mulai.")

        return cleaned_data