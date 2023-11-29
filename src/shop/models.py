from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse("get_checkout_session_id", args=[self.pk])
