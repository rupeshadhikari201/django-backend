# Generated by Django 5.0.2 on 2024-03-28 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0013_alter_projects_skills_required"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectsassigned",
            old_name="frelancers",
            new_name="frelancer_id",
        ),
        migrations.RenameField(
            model_name="projectsassigned", old_name="project", new_name="project_id",
        ),
    ]