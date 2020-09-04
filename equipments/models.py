from django.db import models


class Bunrui(models.Model):
    name = models.CharField(max_length=50)
    bunruiid   = models.IntegerField()

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
  # bunruiid = models.ForeignKey(bunrui, on_delete=models.CASCADE, to_field=bunruiid,default=0)
  eq_type = models.IntegerField()
  owner = models.CharField(max_length=20,default = "ISDL")
  state = models.IntegerField()
  borrower =models.TextField(null= True,blank=True)
  remark = models.TextField(null= True,blank=True)
  

  def __str__(self):
    return self.name

class User(models.Model):
  name = models.CharField(max_length = 50)
  password = models.CharField(max_length = 50)

  def __str__(self):
    return self.name
