from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    hits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()

