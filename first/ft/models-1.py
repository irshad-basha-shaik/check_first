from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import validate_file_extension

# Create your models here.
class UploadFileModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to="documents/%Y/%m/%d", null=True, blank=True, validators=[FileExtensionValidator( ['.xls'] ) ])


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')
    specs = models.FileField(upload_to='specs')