from django.contrib.auth.models import User
from django.db import models
from app.models import *


# Create your models here.
class chat(models.Model):
    doc = models.ForeignKey(User, related_name='related_primary_manual_roats', verbose_name="doc",
                            on_delete=models.CASCADE)
    pa = models.ForeignKey(User, related_name='related_secondary_manual_roats', verbose_name="pa",
                           on_delete=models.CASCADE)
    product = models.ForeignKey(product, blank=True, on_delete=models.CASCADE, null=True)
    sub = models.CharField(max_length=255)
    to = models.IntegerField()
    sts = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
