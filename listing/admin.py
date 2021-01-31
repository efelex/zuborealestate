from django.contrib import admin

# Register your models here.
from .models import Listing, Province,Town, Suburb,ListingType,PropertyType

# admin classes for my model classes
class ListingAdmin(admin.ModelAdmin):
    list_display=('id','description','propertyType','listingType'
        ,'province','town','suburb','price','numberOfBedrooms','numberOfBathrooms',
        'image1'
        ,'image2'
        ,'image3'
        ,'image4'
        ,'image5'
        ,'image6'
        ,'image7'
        ,'image8'
        ,'postedDate','availableDate','is_Available')
class ProvinceAdmin(admin.ModelAdmin):
    list_display=('id','name')

class TownAdmin(admin.ModelAdmin):
        list_display=('id','name')


class SuburbAdmin(admin.ModelAdmin):
        list_display=('id','name')

class ListingTypeAdmin(admin.ModelAdmin):
        list_display=('id','listingType')

class PropertyTypeAdmin(admin.ModelAdmin):
        list_display=('id','propertyType')

# allowing models to be customisable in the django admin 
admin.site.register(Listing,ListingAdmin)
admin.site.register(Province,ProvinceAdmin)
admin.site.register(Town,TownAdmin)
admin.site.register(Suburb,SuburbAdmin)
admin.site.register(ListingType)
admin.site.register(PropertyType)