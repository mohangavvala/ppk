from django.db import models


class Post(models.Model):
    name=models.CharField(max_length=30,default=None)
    mail=models.EmailField(default=None)
    mnumber=models.CharField(max_length=12)
    msg=models.TextField(null=True)