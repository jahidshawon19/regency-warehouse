from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse 
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
	return render(request,"index.html")

##################### CATEGORY VIEWS START #######################
@login_required
def category(request):
	queryset=Category.objects.all()
	totalCat=queryset.count()
	form=CategorySearchForm(request.POST or None)
	if request.method == 'POST':
		queryset=Category.objects.filter(name__icontains=form['name'].value())

	context={
		"queryset":queryset,
		"totalCat":totalCat,
		'form':form,
	}
	return render(request, "categoryList.html", context)
@login_required
def addCategory(request):
	form = CatagoryCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'New Category Added To The List')
		return redirect('category-list')

	context = {
		'form':form,
	}
	return render(request, 'genral_form.html', context)

@login_required
def updateCategory(request,pk):
	queryset = Category.objects.get(id=pk)
	form = CategoryUpdateForm(instance=queryset)
	if request.method=='POST':
		form = CategoryUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Category Updated Successfully')
			return redirect('category-list')

	context = {
		'form':form,

	}
	return render(request, 'genral_form.html', context)

@login_required
def deleteCategory(request,pk):
	queryset = Category.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Category Deleted Successfully')
		return redirect('category-list')
	return render(request, 'genral_delete.html')

##################### CATEGORY VIEWS END #######################




####################### VENDORS VIEWS START ####################
@login_required
def vendor(request):
	queryset= Vendor.objects.all()
	totalVendor = queryset.count()
	form = VendorSearchForm(request.POST or None)
	if request.method == 'POST':
		queryset=Vendor.objects.filter(phone__icontains=form['phone'].value())	
	context= {
		'queryset':queryset,
		'totalVendor':totalVendor,
		'form':form,
	} 
	return render(request, 'vendorList.html', context)
@login_required
def addVendor(request):
	form = VendorCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'New Vendor Added To The List')
		return redirect('vendor-list')

	context ={
		'form':form,
	}
	return render(request, 'genral_form.html', context)


@login_required
def updateVendor(request,pk):
	queryset=Vendor.objects.get(id=pk)
	form = VendorUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = VendorUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Vendor Updated Successfully')
			return redirect('vendor-list')

	context = {
		'queryset':queryset,
		'form':form,
	}
	return render(request, 'genral_form.html', context)


@login_required
def deleteVendor(request,pk):
	queryset = Vendor.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Vendor Deleted Successfully')
		return redirect('vendor-list')
	return render(request, 'genral_delete.html')
####################### VENDORS VIEWS START ####################


############################# ITEM VIEWS START ########################
@login_required
def itemList(request):
	queryset = Stock.objects.all().order_by('created')
	totalItem = queryset.count()
	form = ItemSearchForm(request.POST or None)
	if request.method == 'POST':
		queryset=Stock.objects.filter(itemName__icontains=form['itemName'].value())
		if form['ExportCSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment;filename="List of Item.csv"'
			writer = csv.writer(response)
			writer.writerow(['Category','Item Name','Quantity','Store Date','Last Updated'])
			instance=queryset 
			for stock in instance:
				writer.writerow([stock.category,stock.itemName,stock.quantity,stock.created,stock.lastUpdate])

			return response
	context = {

		'queryset':queryset,
		'totalItem':totalItem,
		'form':form,

	}

	return render(request, 'item_list.html',context)
@login_required
def addItem(request):
	form = ItemCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'New Item Added To The List')
		return redirect('item-list')

	context ={
		'form':form,
	}
	return render(request, 'genral_form.html', context)

@login_required
def updateItem(request,pk):
	queryset=Stock.objects.get(id=pk)
	form = ItemUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ItemUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Item Updated Successfully')
			return redirect('item-list')

	context = {
		'queryset':queryset,
		'form':form,
	}
	return render(request, 'genral_form.html', context)

@login_required
def deleteItem(request,pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Item Deleted Successfully')
		return redirect('item-list')
	return render(request, 'genral_delete.html')
############################# ITEM VIEWS END ########################



############################### ISSUE ITEMS VIEW START ######################
@login_required
def issueItem(request,pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		if instance.quantity>instance.issueQuantity:
			instance.quantity -= instance.issueQuantity
			messages.success(request, "Issued Successfully."+str(instance.quantity)+" "+str(instance.itemName)+"s now left in store")
			instance.save()
			return redirect('item-list')
	context = {
		"queryset":queryset,
		"form":form,
	}
	return render(request, 'genral_form.html', context)

############################### ISSUE ITEMS VIEW END ######################


################################ RECEIVE ITEMS VIEW START #######################
@login_required
def receiveItem(request,pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receiveQuantity
		instance.save()
		messages.success(request, "Receive Successfully."+ str(instance.quantity)+" "+str(instance.itemName)+"s now in store.")
		return redirect('item-list')
	context = {
		'queryset':queryset,
		'form':form,
	}
	return render(request, 'genral_form.html', context)

################################ RECEIVE ITEMS VIEW END #######################