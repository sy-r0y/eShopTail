# Create your models here.

# MODEL represents some real-world concept i.e from the real-world which define our product

from django.db import models
# here from *django.db* PACKAGE .. we are importing the *models* MODULE


# Model class is in the *models* module.
# Model class defines all the common characters/behaviour for any model in a Django app
# Ex- To store the model in a database, read model from the databsae, delete model from database etc
# So, Product class, by inheriting from the Model class.. will also inherit all those features/capabilities

class Product(models.Model):  # Product inherits from Model class

    # define all the attributes, functions of the class Product
    name = models.CharField(max_length=255)  # name is an instance of the CharField class.. can contain textual data
    price = models.FloatField()  # price is an instance of the FloatField class, can contain floating point number
    stock = models.IntegerField()
    # image_url = models.ImageField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    # Offer model would provide offers
    # offers coupon code (text)
    # description about the offer (text)
    # discount .. 0.2 (float)
    # create this model class .. then create migration to bring DB uptodate

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField(max_length=10)


class ExchangeOffers(models.Model):
    exchange_description = models.CharField(max_length=255)
    exchange_price = models.IntegerField()
