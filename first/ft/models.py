from django.db import models
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    xls = models.FileField(null=True,
                           blank=True,
                           validators=[FileExtensionValidator( ['xls'] ) ])