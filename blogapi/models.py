from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    info = models.CharField(max_length=1500, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    articledate = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'

    def __str__(self):
        return self.title + self.author
