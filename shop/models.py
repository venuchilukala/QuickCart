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
    email = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=70, default='')
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc