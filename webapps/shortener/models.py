# shortener/models.py
from django.db import models
from django.utils import timezone
import string
import random

class URL(models.Model):
    original_url = models.URLField()  
    short_url = models.CharField(max_length=10, unique=True, blank=True)  
    custom_url = models.CharField(max_length=10, unique=True, blank=True)  
    expiry_date = models.DateTimeField(null=True, blank=True)  
    access_count = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"

    def save(self, *args, **kwargs):
        if not self.short_url and not self.custom_url:
            self.short_url = self.generate_short_url()
        elif self.custom_url:
            self.short_url = self.custom_url 
        super().save(*args, **kwargs)

    def generate_short_url(self):
        length = 6
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choices(characters, k=length))
        while URL.objects.filter(short_url=short_url).exists():
            short_url = ''.join(random.choices(characters, k=length))
        return short_url

    def is_expired(self):
        return self.expiry_date and timezone.now() > self.expiry_date
