from django.urls import path
from .views import index,IndexDetailView,AboutPageView,ContactPageView,GalleryPageView,ServisPageView,TestPageView,KopPageView,category,post_detaile
from django.conf.urls.static import static 
from django.conf import settings
from .import views

urlpatterns = [

			path('',views.index,name = 'index'),
			path('post_detail/<int:pk>/',IndexDetailView.as_view(),name='post_detail'),
			path('about/',AboutPageView.as_view(),name='about'),
			path('contact/',ContactPageView,name='contact'),
			path('gallery/',GalleryPageView,name='gallery'),
			path('service/',ServisPageView.as_view(),name='service'),
			path('testimonial/',TestPageView.as_view(),name='testimonial'),
			path('kop_mal/',KopPageView.as_view(),name='kop_mal'),
			path('category/<int:category_id>/',category,name='category'),
			path('postdetaile/<int:news_id>/',post_detaile,name='post_detaile'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)