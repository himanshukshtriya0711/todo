from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateField()
    is_completed = models.BooleanField(default=False)


class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile_pic/")  #upload_to is a default argument in image field