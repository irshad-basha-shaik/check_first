from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .forms import handle_uploaded_file
from .models import UploadFileModel


def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #form = UploadFileModel(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            # instance = ModelWithFileField(file_field=request.FILES['file'])
            # instance.save()
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
        #form = UploadFileModel()
    context['form'] = form
    return render(request, 'upload.html', context)

