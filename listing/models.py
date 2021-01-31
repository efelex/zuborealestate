from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class ListingType(models.Model):
    listingType=models.CharField(max_length=255)
    def __str__(self):
         return self.listingType

class PropertyType(models.Model):
    propertyType=models.CharField(max_length=255)
    def __str__(self):
         return self.propertyType


class Province(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
         return self.name


class Town(models.Model):
    name=models.CharField(max_length=255)
    province=models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
         return self.name

class Suburb(models.Model):
     name=models.CharField(max_length=255)
     town=  models.ForeignKey(Town,on_delete=models.CASCADE)
     def __str__(self):
         return self.name

class Listing(models.Model):
    description=models.CharField(max_length=255)
    numberOfBedrooms=models.IntegerField(blank=True)
    numberOfBathrooms=models.IntegerField(blank=True)
    listingType=models.ForeignKey(ListingType,on_delete=models.CASCADE)
    propertyType=models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    province=models.ForeignKey(Province, on_delete=models.CASCADE)
    town=  models.ForeignKey(Town,on_delete=models.CASCADE)
    suburb= models.ForeignKey(Suburb,on_delete=models.CASCADE,blank=True)
    price=models.FloatField()
    image1=models.CharField(max_length=255)
    image2=models.CharField(max_length=255,blank=True)
    image3=models.CharField(max_length=255,blank=True)
    image4=models.CharField(max_length=255,blank=True)
    image5=models.CharField(max_length=255,blank=True)
    image6=models.CharField(max_length=255,blank=True)
    image7=models.CharField(max_length=255,blank=True)
    image8=models.CharField(max_length=255,blank=True)
    postedDate=models.DateTimeField(default=timezone.now)
    availableDate=models.DateField(default=date.today)
    is_Available=models.BooleanField(default=True)
    
    def __str__(self):
        return "ZMW " + str(self.price) + '  ' + self.description
        #  f"{self.price} {self.description}"
        #  "% s" % self.price + '  ' + self.description
    
    


# Description summary
# Property listing id
# -type#(flat,standalone,complex)
# -listing type (rent/ sale)
# -number of bedrooms
# -number of bathrooms
# -location: province,town,suburb
# -rentprice /sale price
# -images
# Image2
# Image3
# Image4



