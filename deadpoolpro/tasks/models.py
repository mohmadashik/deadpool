from django.db import models

# Create your models here.

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20,default='pending')


    def __str__(self):
        return self.title