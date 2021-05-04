from django import forms
from .models import*

class CatagoryCreateForm(forms.ModelForm):
	class Meta:
		model = Category 
		fields= ['name',]

class CategoryUpdateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name',]




class VendorCreateForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields=['company','name','phone','email']


class VendorUpdateForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields=['company','name','phone','email']
