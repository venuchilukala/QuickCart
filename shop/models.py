from django.db import models

# Create your models here.
      
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)  # New field for discount price
    brand = models.CharField(max_length=50, default='')  # New field for brand
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, unique=True, default='')  # Set email as unique
    phone = models.CharField(max_length=70, default='')
    desc = models.TextField()

    def __str__(self):
        return self.name
