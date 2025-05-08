from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()
    created_time = models.DateTimeField(default=timezone.now)
    #user = CustomUser

    def __str__(self):
        return self.title


class PostReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    cover_picture = models.ImageField(default='default_cover_pic.jpg')
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)


