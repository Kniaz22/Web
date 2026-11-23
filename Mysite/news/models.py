from django.db import models

class News(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title