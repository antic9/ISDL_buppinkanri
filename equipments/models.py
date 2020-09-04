from django.db import models

class Bunrui(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
        
class Equipment(models.Model):\

  name = models.CharField(max_length=50)
  owner = models.CharField(max_length=20,default = "ISDL")
  bunrui = models.ForeignKey(Bunrui, on_delete=models.CASCADE, default='')
  borrower = models.TextField(null= True,blank=True,default='')
  state = models.IntegerField(default=0)
  remark = models.TextField(null= True,blank=True)

  def __str__(self):
    return self.name 
  
  class Meta:
    ordering = ['name']

class User(models.Model):
  name = models.CharField(max_length = 50)
  password = models.CharField(max_length = 50)

  def __str__(self):
    return self.name

