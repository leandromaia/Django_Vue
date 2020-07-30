from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    boolean = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads')
