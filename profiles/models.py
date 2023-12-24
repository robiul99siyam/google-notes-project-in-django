from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WriteModel(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title