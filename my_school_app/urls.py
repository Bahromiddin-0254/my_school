from django.urls import path
from .views import *

app_name = 'm_sch_app'
urlpatterns = [
    path('',IndexView.as_view(),name='IndexView'),
    path('about/',AboutView.as_view(),name='AboutView'),
    path('contact/',ContactView.as_view(),name='ContactView'),
    path('price',PriceView.as_view(),name='PriceView'),
    path('videos',VideosView.as_view(),name='VideosView'),
    path('sidebar_right/',Sidebar_rightView.as_view(),name='Sidebar_rightView'),
    path('courses/',CoursesView.as_view(),name='CoursesView'),
]