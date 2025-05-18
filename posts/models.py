from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class PostAuthor(models.Model):
    post = ForeignKey(Post, on_delete=models.CASCADE)
    author = ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.post.title} by {self.author.last_name} {self.author.first_name}"


class PostReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    cover_picture = models.ImageField(default='default_cover_pic.jpg')
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
          return f"{self.stars_given} stars to this book by {self.user}"

