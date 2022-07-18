from django.db import models
from ..accounts.models import Account


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Timestamp):
    image = models.ImageField(upload_to='categories/', null=True)
    title = models.CharField(max_length=221)

    @property
    def normalize_title(self):
        return self.title.replace(' ', '').lower()

    def __str__(self):
        return self.title


class Product(Timestamp):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=221)
    price = models.FloatField()
    views = models.IntegerField(default=0)
    mid_rate = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return f'{self.id} | {self.name}'

    @property
    def get_mid_rate(self):
        rates = self.rate_set.all()
        mid = 0
        try:
            mid = sum([i.rate for i in rates]) / rates.count()
        except ZeroDivisionError:
            pass
        self.mid_rate = mid
        self.save()
        return mid


class ProductImage(Timestamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return f'image of {self.product}'


class Rate(Timestamp):
    RATE = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE, default=0)

    def __str__(self):
        return f'rate of {self.user.email}'
