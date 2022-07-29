from django.db import models

class QRimg(models.Model):
    # text = models.CharField(max_length=300)
    file = models.ImageField(upload_to="upload", max_length=None)