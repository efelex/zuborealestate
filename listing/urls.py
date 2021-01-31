from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='listing-home'),
    path('about', views.about,name='listing-about'),
    path('<int:listing_id>',views.detail ,name='listing-detail'),
]