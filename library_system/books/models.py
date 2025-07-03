from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    price = models.FloatField()
    total_copies = models.PositiveIntegerField(default=1)
    pages = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.TextField()
    email=models.EmailField()

    def __str__(self):
        return self.user.username