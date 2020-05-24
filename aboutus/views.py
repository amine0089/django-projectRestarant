from django.shortcuts import render
from .models import AboutUs, Why_Choose_Us,Chef

def aboutus_list(request):
	about = AboutUs.objects.last()
	chef = Chef.objects.all()
	why_choose_us = Why_Choose_Us.objects.all()
	context = {
			'about':about,
			'chef':chef,
			'why_choose_us':why_choose_us,
	}
	return render(request,'aboutus/about.html',context)

