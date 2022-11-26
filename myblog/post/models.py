from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Posts(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'published')
    )

    title = models.CharField(max_length=250, unique=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES,default='published',max_length=10)
    category = models.CharField(max_length=500, default='coding')


    class Meta:
        ordering =('publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})      


# Model for Categories
class Categories(models.Model):
    name = models.CharField(max_length=500)


    class Meta:
        db_table = 'Category'

    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('home')    


           