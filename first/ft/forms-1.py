from django import forms
from .validators import validate_file_extension
from .models import Car


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50,required=False)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class CarForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    photo = forms.ImageField()
    specs = forms.FileField()

    def clean(self):
        cleaned_data = super(CarForm, self).clean()
        self.instance.field = 'value'
        return cleaned_data

    class Meta:
        model = Car
        fields = ['name', 'price', 'photo', 'specs']
def handle_uploaded_file(f):
    with open('/dev-data/Projects/checking/example.xls', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
