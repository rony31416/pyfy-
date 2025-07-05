from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    cover_url = models.URLField(max_length=200, blank=True)
    language = models.CharField(max_length=50, default='English')

    def __str__(self):
        return self.title