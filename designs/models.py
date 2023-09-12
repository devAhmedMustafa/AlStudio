from django.db import models
from datetime import datetime
from uuid import uuid4
from django.contrib.auth.models import User
from PIL import Image

class Album(models.Model):
    uuid = models.UUIDField(default=uuid4(), unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='albums/covers/')

class Design(models.Model):
    uuid = models.UUIDField(default=uuid4(), unique=True, primary_key=True)
    img = models.ImageField(upload_to="designs/%y/%m/%d/")
    title = models.CharField(max_length=1000)
    desc = models.TextField(blank=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    publish_date = models.DateTimeField(default=datetime.now())
    album = models.ManyToManyField(Album, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        if img.height > 900:
            output_size = (img.width,900)
        if img.width > 900:
            output_size = (300,img.height)
            img.thumbnail(output_size)
            img.save(self.img)

    def __str__(self):
        return f"{self.title}"

class Like(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, related_name='design')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by')

    def __str__(self):
        return f"{self.liked_by.username} | {self.design.title}"

    class Meta:
        unique_together = ['design', 'liked_by']

class Save(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)