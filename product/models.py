from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.OneToOneField(
        Category,
        on_delete=models.DO_NOTHING,
        parent_link=False,
        null=True,
        blank=True,
        related_name='category',
    )
    sku = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    gender = models.CharField(
        max_length=1,
        choices=(('M', 'Male'), ('F', 'Female')),
    )

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='variant', on_delete=models.CASCADE)
    size = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=30)
    color_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name
