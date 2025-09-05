from django.db import models
from users.models import User 
from product.models import Product
from uuid import uuid4


# - - - - - - - - - #
#     Cart Model    #
# - - - - - - - - - #
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.first_name}"
    



# - - - - - - - - - - - #
#     CartItem Model    #
# - - - - - - - - - - - #
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    

    
    
# - - - - - - - - - #
#     Order Model   #
# - - - - - - - - - #
class Order(models.Model):
    PENDING = 'Pending'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2 
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    



# - - - - - - - - - - - #
#     OrderItem Model   #
# - - - - - - - - - - - #
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"