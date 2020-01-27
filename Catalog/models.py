from django.db import models

# Create your models here.
# Create Product Field
class Product(models.Model):
     name = models.CharField(max_length=200, blank=False)
     price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
     stock = models.IntegerField(blank=False)
     
     def __str__(self):
               return self.name + " $" + str(self.price) + " (x" + str(self.stock) + ")"

# Create Category Field
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return "{} (id: {})".format(self.name, self.id)
        #return self.name + "( id:"+self.id+")"

