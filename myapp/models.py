from django.db import models
import uuid
from datetime import datetime
# Create your models here.
class SliderModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    contact = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.contact

class AboutModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class BlogModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    img = models.ImageField(default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class ClientModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    img = models.ImageField(default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10, null=True, blank=True)
    phone = models.TextField(max_length=15,null=True)
    email = models.EmailField()
    meassage = models.TextField() 
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name