from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.TextField()
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


