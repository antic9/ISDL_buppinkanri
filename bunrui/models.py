from django.db import models

# Create your models here.
class bunrui(models.Model):
    name = models.CharField(max_length=50)
    bunruiid   = models.IntegerField()

    def __str__(self):
        return self.name