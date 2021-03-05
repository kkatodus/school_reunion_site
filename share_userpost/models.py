from django.db import models
from user.models import CustomUser

# Create your models here.

class UserPost(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,default=1,on_delete=models.CASCADE)
    post_text = models.CharField(max_length=60)
    class Meta():
        verbose_name_plural="UserPost"
    
class Picture(models.Model):
    image = models.ImageField(upload_to="photos/")
    post = models.ForeignKey(UserPost,default=1,on_delete=models.CASCADE)
