from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    phone = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='boy.png')
    location = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    
class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images')
    name = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    create_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.user
        
    