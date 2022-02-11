from django.db import models

class QRimg(models.Model):
    file = models.ImageField(upload_to="upload", max_length=None)