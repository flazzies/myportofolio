from django.db import migrations

def add_initial_data(apps, schema_editor):
    Skill = apps.get_model('main', 'Skill')
    Experience = apps.get_model('main', 'Experience')

    Skill.objects.get_or_create(
	name="Java",
	category="backend",
	proficiency="intermediate",
	description="Berpengalaman dalam pengembangan perangkat lunak berbasis OOP, abstraksi class hierarchy, dan perancangan logika backend.",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg",
    )

    Skill.objects.get_or_create(
	name="Python",
	category="backend",
	proficiency="intermediate",
	description="Terlatih menerapkan konsep fundamental pemrograman, algoritma dasar, dan paradigma fungsional/prosedural Python untuk membangun modul aplikasi web yang efisien dan bersih.",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg")

    Skill.objects.get_or_create(
	name="CSS",
	category="frontend",
	proficiency="beginner",
	description="Mampu mengelola estetika komponen antarmuka, menyelaraskan tema visual, dan menerapkan media queries dasar untuk mendukung tampilan web yang adaptif.",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg")

    Skill.objects.get_or_create(
	name="HTML",
	category="frontend",
	proficiency="beginner",
	description="Menguasai dasar-dasar penulisan markup standar, manajemen atribut elemen, dan penyusunan kerangka halaman yang siap diintegrasikan dengan penataan CSS maupun template backend.",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg")

    Skill.objects.get_or_create(
	name="Django",
	category="backend",
	proficiency="beginner",
	description="Memahami konsep arsitektur MVT (Model-View-Template), konfigurasi routing URL terstruktur, dan rendering data dinamis ke dalam template web menggunakan tag Django. ",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg")


    Skill.objects.get_or_create(
	name="BASH",
	category="devops",
	proficiency="beginner",
	description="Terbiasa mengoperasikan terminal Unix/Bash untuk mengelola virtual environment, menjalankan perintah server Django, serta mengeksekusi alur kerja kontrol versi Git secara efisien.",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg")

    Skill.objects.get_or_create(
	name="SQL",
	category="database",
	proficiency="beginner",
	description="Memahami prinsip dasar basis data relasional, perancangan skema tabel menggunakan DDL, serta penulisan sintaks DML untuk menjalankan operasi CRUD secara terstruktur. ",
    thumbnail="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azuresqldatabase/azuresqldatabase-original.svg")


    


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),  # Pastikan nama ini sesuai file migrasi sebelumnya
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]