# mywork/models.py file
import os
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects", blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # workdone_date = models.DateTimeField()
    technologies = models.CharField(
        max_length=200,
        blank=True,
        help_text="Comma-separated list of technologies used",
    )
    featured = models.BooleanField(
        default=False, help_text="Feature this project on the homepage"
    )
    category = models.CharField(
        max_length=50,
        blank=True,
        choices=[
            ("Python", "Django & Flask"),
            ("Javascript", "React, MERN, NEXT.JS"),
            ("Core", "Custom CSS, JS & HTML"),
            ("design", "UI/UX Design"),
        ],
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.image and not self.pk:
            file_extension = os.path.splitext(self.image.name)[1]
            safe_filename = f"{slugify(self.title)}{file_extension}"
            self.image.name = safe_filename
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
