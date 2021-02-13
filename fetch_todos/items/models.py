from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(unique=True, max_length=25)

    def __str__(self):
        return self.item
