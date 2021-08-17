from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def short_view(self):
        return f"{self.body[:70]} ..."

