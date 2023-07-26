from django.urls import path
from testimonial import views 
urlpatterns = [
    path('',views.index,name='index'),
]