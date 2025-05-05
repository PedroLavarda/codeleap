from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment on {self.post.title} by {self.post.username}"