from django.shortcuts import render,get_object_or_404
from .models import Listing

from django.http import HttpResponse,Http404
# Create your views here.


listings =[
    {
    'listing_id':'1234',
    'location':'chilenge',
    'image1':'https://images.prop24.com/252485424/Crop676x507',
    'price':'2400',
    'bathrooms':'2',
    'master_self_contained':'yes'

    },
    {
    'listing_id':'12345',
    'location':'chilanga',
    'image1':'https://images.prop24.com/254091440/Crop676x507',
    'price':'2500',
    'bathrooms':'1',
    'master_self_contained':'no'

    }
 ]
def index(request):
    listings=Listing.objects.all()
    # listings=Listing.objects.
    render(request,'listing/listingHome.html',context)

def home(request):
    listings=Listing.objects.all()
    # select * from listing_listing 
    return render(request,'listing/listingHome.html',{'listings':listings})
# def  home(request):
#     context = {
#         'listings':listings
#         }
#     return render(request,'listing/listingHome.html',context)
   
def detail(request,listing_id):
    try:
        listing=get_object_or_404(Listing,pk=listing_id)
        return  render(request,'listing/detail.html',{'listing':listing})
    except Listing.DoesNotExist:
        raise Http404()
    # HttpResponse('<h1> Welcome to Zubo Realestates</h1>')


def about(request): 
    return  render(request,'listing/about.html',{'title':'About'})
    
    # HttpResponse('<h1> About Zubo Realestates</h1>')