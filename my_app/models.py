from django.db import models
from ckeditor.fields import RichTextField

class Mebel(models.Model):
	nomi = models.CharField(max_length=250)
	text = RichTextField(blank=True)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.nomi



class Comment(models.Model):
	username = models.CharField(max_length=150,null=True)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=250)
	message = RichTextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.username



class Category(models.Model):
	name = models.CharField(max_length=250,null = False,blank = False)


	def __str__(self):
		return self.name



class News(models.Model):
	title = models.CharField(max_length=250,null = False,blank = False)
	image = models.ImageField(upload_to='images/', blank = True)
	text = RichTextField()
	category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__ (self):
		return self.title



class Raz(models.Model):
	ism = models.CharField(max_length=50,blank=True)
	text4 = models.TextField()
	rasm = models.ImageField(upload_to='images/',blank=True)

	def __str__ (self):
		return self.ism