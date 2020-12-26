from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View

#from .models import *
#from django.shortcuts import get_object_or_404

#from .forms import CommentForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request,'index.html')
class VideosView(View):
    def get(self,request):
        return render(request,'videos.html')
class ContactView(View):
    def get(self, request):
        return render(request,'contact.html')
class Sidebar_rightView(View):
    def get(self,request):
        return render(request,'sidebar-right.html')
class AboutView(View):
    def get(self, request):
        return render(request,'about.html')
class CoursesView(View):
    def get(self,request):
        return render(request,'courses.html')
class PriceView(View):
    def get(self,request):
        return render(request,'price.html')