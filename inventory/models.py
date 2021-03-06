from django.db import models

# Create your models here.
class Device(models.Model): #name of the table
    type = models.CharField(max_length=100, blank=False) # name of the column
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item is available for use'),
        ('OUT OF ORDER', 'Item is not working properly'),
        ('IN-USE', 'Item is being used by employee'),
        ('DECOMMISSIONED', 'Item has been decommissioned')
    )
    status = models.CharField(max_length=15, choices=choices, default="AVAILABLE") # available, sold, restocking
    issues = models.CharField(max_length=100, default="ENTER ISSUES")
    user = models.CharField(max_length=100, default="USER")
    location = models.CharField(max_length=10, default="LOCATION")
    assetNum = models.CharField(max_length=20, default="ASSET NUMBER")
    serviceTag = models.CharField(max_length=20, default="SERVICE TAG" )

    def __str__(self):
        return 'Type : {0} Price : {1} User : {2} Part Number : {3} Location : {4}'.format(self.type, self.price, self.user, self.assetNum, self.location)


    class Meta:
        abstract = True


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass

class Equipment(Device):
    pass
