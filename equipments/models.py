from django.db import models

class Bunrui(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField

    def __str__(self):
        return self.name
        
class Equipment(models.Model):
    
  # eq_type
  BOOK = 1
  DEVICE = 2
  COMPUTER = 3

  # state
  NOT_ON_LOAN = 0
  ON_LOAN = 1
  REQUESTING = 2
  
  name = models.CharField(max_length=50)
  eq_type = models.IntegerField()
  owner = models.CharField(max_length=20,default = "ISDL")
  state = 0
  borrower = ""
  remark = models.TextField(null= True,blank=True)

  def __str__(self):
    return self.name

class User(models.Model):
  name = models.CharField(max_length = 50)
  password = models.CharField(max_length = 50)

  def __str__(self):
    return self.name

