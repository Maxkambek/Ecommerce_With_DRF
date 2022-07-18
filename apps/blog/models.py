from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='posts/', null=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
