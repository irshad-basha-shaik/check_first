from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
import pyexcel as pe
from django.conf import settings
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			name = form['xls'].name
			#sheet = pe.get_sheet(file_name=os.path.join(base_dir, "example.xls"), name_columns_by_row=0)
			newdoc = form.save(commit=False)
			newdoc.save()

			return index(request)
	else:
		form = PostForm()
	return render(request,"index.html",{"form":form})

def index(request):
	#form = PostForm(instance=obj)
	list = Post.objects.all()
	# if request.method == 'POST':
	# 	form = PostForm(request.POST)
	# 	if form.is_valid():
			# if request.POST['hdd1'] != '':
			# 	form.cleaned_data['hdd'] = request.POST['hdd1']
			# elif request.POST['hdd2'] != '':
			# 	form.cleaned_data['hdd'] = request.POST['hdd2']
			# elif request.POST['hdd3'] != '':
			# 	form.cleaned_data['hdd'] = request.POST['hdd3']
			# AssetModel.objects.filter(pk=id).update(location=form.cleaned_data['location'],asset_no=form.cleaned_data['asset_no'],emp_id=form.cleaned_data['emp_id'],usage_type=form.cleaned_data['usage_type'],machine_type=form.cleaned_data['machine_type'],gef_id_number=form.cleaned_data['gef_id_number'],domain_workgoup=form.cleaned_data['domain_workgoup'],machine_make=form.cleaned_data['machine_make'],machine_model_no=form.cleaned_data['machine_model_no'],machine_serial_no=form.cleaned_data['machine_serial_no'],hdd=form.cleaned_data['hdd'],hdd_make=form.cleaned_data['hdd_make'],hdd_model=form.cleaned_data['hdd_model'],hdd_serial_no=form.cleaned_data['hdd_serial_no'],ram=form.cleaned_data['ram'])
			# Post(xls=form.cleaned_data['xls'])
	return render(request, "upload.html", {"list": list})




def handle_uploaded_file(f):
    with open(f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def main(base_dir):
# 	sheet = pe.get_sheet(file_name=os.path.join(base_dir, "example.xls"), name_columns_by_row=0)
# 	print(sheet.to_dict())
#
# 	sheet.column.format(0, str)
# 	print(sheet.to_dict())
#
#
# if __name__ == '__main__':
# 	main(os.getcwd())