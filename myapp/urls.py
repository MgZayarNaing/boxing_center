from django.urls import path 
from myapp.views import  HomeSection,AboutSection,BlogSection

urlpatterns = [
    path('home/', HomeSection),
    path('about/', AboutSection),
    path('blog/', BlogSection),

]