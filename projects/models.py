from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='technologies')
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    image = models.FileField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title
