from django.db import models

class Page(models.Model):
   title = models.CharField(max_length=255)

   def __str__(self):
       return self.title

class Imgs(models.Model):
    imgs = models.FileField(upload_to='minuta/', blank=True, null=True)

    def __str__(self):
        return str(self.imgs)

