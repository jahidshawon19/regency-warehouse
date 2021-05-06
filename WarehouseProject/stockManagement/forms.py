from django import forms
from .models import*

class CatagoryCreateForm(forms.ModelForm):

	class Meta:
		model = Category 
		fields= ['name',]

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This Field Is Required!')
		for instance in Category.objects.all():
			if instance.name == name:
				raise forms.ValidationError(name+ ' already created!')


		return name

class CategoryUpdateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name',]


class CategorySearchForm(forms.ModelForm):
	class Meta:
		model=Category
		fields = ['name']

class VendorCreateForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields=['company','name','phone','email']

	def clean_company(self):
		company = self.cleaned_data.get('company')
		if not company:
			raise forms.ValidationError('This Field Is Required!')
		return company




class VendorUpdateForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields=['company','name','phone','email']


class VendorSearchForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields=['phone']





class ItemCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields =['category','itemName','quantity']

	def clean_category(self):
		category = self.cleaned_data.get('category')
		if not category:
			raise forms.ValidationError('This Field Is Required!')

		return category

	def clean_itemName(self):
		itemName = self.cleaned_data.get('itemName')
		if not itemName:
			raise forms.ValidationError('This Field Is Required!')

		for x in Stock.objects.all():
			if x.itemName == itemName:
				raise forms.ValidationError(itemName+ ' already created!')
			
		return itemName


class ItemUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ['category','itemName','quantity']



class ItemSearchForm(forms.ModelForm):
	ExportCSV=forms.BooleanField(required=False)
	class Meta:
		model=Stock
		fields = ['itemName']




class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ['issueQuantity', 'issueTo']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ['receiveQuantity', 'receiveBy']