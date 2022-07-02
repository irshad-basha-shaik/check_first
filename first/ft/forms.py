from django.forms import ModelForm
from .models import *
from django import forms
import os
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    def validate(self, value):
        super().validate(value)
        file_extension = os.path.splitext(value.name)[1]
        if file_extension != '.xls':
            raise ValidationError(
                ('Invalid file extension'),
                code='invalid'
            )
    class Meta:
        model = Post
        fields = ['xls']


