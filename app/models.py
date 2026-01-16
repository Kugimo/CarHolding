from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Car(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/car_images', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title