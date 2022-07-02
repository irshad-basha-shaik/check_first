from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm,CarForm,handle_uploaded_file
from .models import UploadFileModel,Car


def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        #form = UploadFileModel(request.POST, request.FILES)
        # handle_uploaded_file(request.FILES['file'])
        instance = Car(photo=request.FILES['photo'])
        instance = Car(specs=request.FILES['specs'])
        instance.save()
        # form.save()
        return HttpResponseRedirect('/success/url/')
    context["form"] = CarForm()
    return render(request, 'upload.html', context)

