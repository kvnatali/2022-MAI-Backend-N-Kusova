from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.title

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=None)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['first_name']