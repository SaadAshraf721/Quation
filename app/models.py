from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class menu(models.Model):
    name = models.CharField(max_length=50)
    sts = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class category(models.Model):
    name = models.CharField(max_length=50)
    sts = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class product(models.Model):
    menu = models.ForeignKey(menu, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='uploads/')
    create_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    sts = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class productImage(models.Model):
    product = models.ForeignKey(product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='uploads/')



class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)


class count(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    viewers = models.IntegerField()
