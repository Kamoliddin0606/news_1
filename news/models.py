from enum import unique
from operator import mod
from turtle import title
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField(upload_to='category/')
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=250)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    title = models.CharField(max_length=120)
    anons = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    
    def __str__(self) -> str:
        return self.title

class Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.news.title} {self.like}'
    

class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    reply_comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.body[:20]}'




