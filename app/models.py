from django.db import models

# Create your models here.

class Submitproperty(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50)
    bhk = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    bedroom=models.CharField(max_length=50)
    kitchen = models.CharField(max_length=50)
    hall = models.CharField(max_length=20)
    bathroom=models.CharField(max_length=50)
    balcony=models.CharField(max_length=50) 
    floorap = models.CharField(max_length=20,default="")
    price=models.IntegerField()
    area_size = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50,default="")
    Address=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    feature =models.CharField(max_length=300,default="")
    img1 = models.ImageField(upload_to="Apartment/images",default="")
    img2 = models.ImageField(upload_to="Apartment/images",default="")
    img3 = models.ImageField(upload_to="Apartment/images",default="")
    img4 = models.ImageField(upload_to="Apartment/images",default="")
    img5 = models.ImageField(upload_to="Apartment/images",default="")
    floor_planimg = models.ImageField(upload_to="Apartment/images",default="")
    status2 = models.CharField(max_length=20)
    groundfloorimg = models.ImageField(upload_to="Apartment/images",default="")
    basementfloor = models.ImageField(upload_to="Apartment/images",default="")
    isfeatured = models.CharField(max_length=50,default="") 
    date = models.CharField(max_length=30,default="")
    ownername=models.CharField(max_length=50,default="")
    # ownername=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Contacts(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.CharField(max_length=50)
    comment=models.CharField(max_length=200)
    def __str__(self):
        return self.name
 
class Feedback(models.Model):
    fullname=models.CharField(max_length=50)
    phone=models.IntegerField()
    feedback=models.CharField(max_length=300)
    def __str__(self):
        return self.fullname


class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    alternative_phone =models.IntegerField()
    address = models.CharField(max_length=100)
    propertyname=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name





