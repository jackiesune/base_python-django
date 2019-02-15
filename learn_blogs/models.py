from django.db import models


class Topic(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


# Create your models here.
