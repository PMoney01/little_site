from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from .models import Mebel,Comment,Category,News,Raz
import requests
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404



class IndexDetailView(DetailView):
	model = Mebel 
	template_name = 'post_detail.html'


class AboutPageView(ListView):
	model = Mebel
	template_name = 'about.html'


class ServisPageView(ListView):
	model = Mebel
	template_name = 'service.html'


class TestPageView(ListView):
	model = Raz
	template_name = 'testimonial.html'


class KopPageView(ListView):
	model = Mebel 
	template_name = 'kop_mal.html'



def telegram_bot_sendtext(bot_message):
	bot_token = '742165651:AAE5wmfl0isYOKlfzidVOvnm-lrA_3HwB88'
	bot_ChatID = '173497942'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_ChatID+'&parse_mode=Markdown&text='+bot_message
	response = requests.get(send_text)
	
	return response.json()



def ContactPageView(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		email = request.POST.get('email', None)
		message = request.POST.get('message', None)
		user = Comment.objects.create(
				username = name,
				phone = phone,
				email = email,
				message = message
			)
		user.save()
		telegram_bot_sendtext(f"Ismi: {name}\nTelefon raqami: {phone}\nEmail: {email}\nXabar: {message}")



	return render(
	request=request,
	template_name = 'contact.html'
	)



def GalleryPageView(request):
	obj = Mebel.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,7)
	try:
		page = p.page(page_n)
	except EmptyPage:
		page = p.page(1)

	context = {
		'page': page
	}
	return render(request, 'gallery.html',context)



def category(request,category_id):
	string = Category.objects.get(pk=category_id)
	string1 = News.objects.all().filter(category_id=category_id)
	if len(string1)>0:
		b = string1[0]
	else:b={}
	states = {
		'asd':string1,
		'st':string,
		'b':b
	}
	return render(request, "category.html", states)



def post_detaile(request,news_id):
	stri = get_object_or_404(News,pk=news_id)
	string1 = News.objects.all().filter(category_id=news_id)


	ctx = {
		'new':stri,
		'asd':string1,
	}
	return render(request, "post_detaile.html", ctx)



def index(request):
	if 'q' in request.GET:
		q = request.GET['q']
		data = Mebel.objects.filter(nomi__icontains=q)
	else:
		data = Mebel.objects.all()
		data1 = Raz.objects.all()
	context = {
		"data" : data,
		"data1":data1
		}

	return render(request, "index.html", context)


