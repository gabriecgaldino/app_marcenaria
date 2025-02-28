from django.db import models
from django.contrib.auth.models import User

class Users(User):
    function = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(
    upload_to='profile_pics/', 
    default='default_profile_image.jpg',  # Imagem padrão
    null=True, 
    blank=True
    )

    def __str__(self):
        return self.first_name
