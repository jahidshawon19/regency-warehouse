from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
	return render(request,"index.html")

##################### CATEGORY VIEWS START #######################
def category(request):
	queryset=Category.objects.all()
	totalCat=queryset.count()
	context={
		"queryset":queryset,
		"totalCat":totalCat,
	}
	return render(request, "categoryList.html", context)

def addCategory(request):
	form = CatagoryCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('category-list')

	context = {
		'form':form,
	}
	return render(request, 'genral_form.html', context)


def updateCategory(request,pk):
	queryset = Category.objects.get(id=pk)
	form = CategoryUpdateForm(instance=queryset)
	if request.method=='POST':
		form = CategoryUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('category-list')

	context = {
		'form':form,

	}
	return render(request, 'genral_form.html', context)


def deleteCategory(request,pk):
	queryset = Category.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('category-list')
	return render(request, 'genral_delete.html')

##################### CATEGORY VIEWS END #######################




####################### VENDORS VIEWS START ####################
def vendor(request):
	queryset= Vendor.objects.all()
	totalVendor = queryset.count()

	context= {
		'queryset':queryset,
		'totalVendor':totalVendor,
	} 
	return render(request, 'vendorList.html', context)

def addVendor(request):
	form = VendorCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('vendor-list')

	context ={
		'form':form,
	}
	return render(request, 'genral_form.html', context)



def updateVendor(request,pk):
	queryset=Vendor.objects.get(id=pk)
	form = VendorUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = VendorUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('vendor-list')

	context = {
		'queryset':queryset,
		'form':form,
	}
	return render(request, 'genral_form.html', context)



def deleteVendor(request,pk):
	queryset = Vendor.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('vendor-list')
	return render(request, 'genral_delete.html')
####################### VENDORS VIEWS START ####################