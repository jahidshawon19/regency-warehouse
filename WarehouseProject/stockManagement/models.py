from django.db import models

# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=50,blank=True,null=True)
	storeDate=models.DateTimeField(auto_now_add=True)
	lastUpdate=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.name



class Vendor(models.Model):
	company = models.CharField(max_length=50,blank=True,null=True)
	name = models.CharField(max_length=50,blank=True,null=True)
	phone = models.CharField(max_length=11,blank=True,null=True)
	email = models.EmailField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	lastUpdate=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.company



class Stock(models.Model):
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	itemName= models.CharField(max_length=50,blank=True,null=True)
	quantity= models.IntegerField()
	receiveQuantity=models.IntegerField()
	receiveBy=models.CharField(max_length=50,blank=True,null=True)
	issueQuantity=models.IntegerField()
	issueBy=models.CharField(max_length=50,blank=True,null=True)
	issueTo=models.ForeignKey(Vendor,on_delete=models.CASCADE, null=True,related_name='ven')
	phone=models.ForeignKey(Vendor,on_delete=models.CASCADE, null=True,related_name='phn')
	createdBy=models.CharField(max_length=50,blank=True,null=True)
	exportToCSV=models.BooleanField(default=False)
	lastUpdate=models.DateTimeField(auto_now_add=False,auto_now=True)
	created=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.itemName