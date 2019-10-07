from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)


class Blog:
    title = 'Hello world'
    content = 'something cool'

