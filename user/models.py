from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="user/media/uploads/", blank=True, null=True)
   


