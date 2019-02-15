from django.db import models


class Topic(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    text=models.TextField()

    class Meta:
        verbose_name_plural="Entries"

    def __str__(self):
        return self.text[:20]+"..."




# Create your models here.
