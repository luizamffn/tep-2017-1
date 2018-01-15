from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    geo = models.ForeignKey(Geo)

class Pessoa(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.ForeignKey(Address, null=True)
    user = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return "%s posted %s" % (self.user.username, self.title)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
