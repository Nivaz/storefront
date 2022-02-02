from django.db import models

# Create your models here

#Promotions class

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

#Collection class

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    
#Product class

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

   

#Customer class

class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    product = models.ForeignKey(Product, on_delete=models.PROTECT)


#Address - customer address class

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)



#Order class

class Order(models.Model):

    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Payment pending'),
        (PAYMENT_COMPLETE, 'Payment complete'),
        (PAYMENT_FAILED, 'Payment failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


#Cart class

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)



#Item class

class Item(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.PositiveSmallIntegerField()