from django.db import models

# Create your models here.

class CourseModuleItem(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)