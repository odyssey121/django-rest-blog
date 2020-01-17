from django.contrib.auth.models import AbstractUser
from django.db import models
from os.path import join
import uuid

def customer_image_file_path(instande, filename):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return join('upload/avatars/', filename)

# Create your models here.
class UserProfile(AbstractUser):

    bio = models.TextField(max_length=255, blank=True)
    avatar = models.ImageField(null=True, upload_to=customer_image_file_path)

    def __str__(self):
        return f'{self.username}'
