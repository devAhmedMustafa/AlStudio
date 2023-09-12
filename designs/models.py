from io import BytesIO
from django.core.files import File
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

    def compress(self, image):    
        im = Image.open(image)   
        im_io = BytesIO()     
        im.save(im_io, 'JPEG', quality=30)    
        new_image = File(im_io, name=image.name)  
        return new_image

    def save(self, *args, **kwargs):
        compImg = self.compress(self.img)
        self.img = compImg
        super().save(*args, **kwargs)

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