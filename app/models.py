from __future__ import unicode_literals
from django.db import models

  

class login_tb(models.Model):
    lid=models.IntegerField(primary_key=True)
    user=models.CharField(max_length=30)
    passw=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)
#--------------registration-------------------------------------------
class user_tb(models.Model):
    lid=models.IntegerField(primary_key=True)
    u_lid=models.IntegerField()
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    gender=models.CharField(max_length=7)
    date=models.DateField()
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=15)
    passw=models.CharField(max_length=30)
    add=models.TextField(max_length=130)

class phar_tb(models.Model):
    lid=models.IntegerField(primary_key=True)
    p_lid=models.IntegerField()
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=15)
    passw=models.CharField(max_length=30)

class maker_tb(models.Model):
    lid=models.IntegerField(primary_key=True)
    p_lid=models.IntegerField()
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    licence=models.IntegerField()
    contact=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=15)
    passw=models.CharField(max_length=30)

class stock(models.Model):
    lid=models.IntegerField(primary_key=True)
    s_lid=models.IntegerField()
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    code=models.IntegerField()
    stock=models.IntegerField()
    des=models.TextField(max_length=120)
    typ=models.CharField(max_length=15)
    rate=models.CharField(max_length=8)

class order(models.Model):
    lid=models.IntegerField(primary_key=True)
    o_lid=models.IntegerField()
    name=models.CharField(max_length=30)
    typ=models.CharField(max_length=15)
    status=models.CharField(max_length=15)
    rate=models.CharField(max_length=7)
    track=models.CharField(max_length=15)
    address=models.TextField(max_length=120)

class register(models.Model):
    lid=models.IntegerField(primary_key=True)
    users=models.IntegerField()
    stock=models.IntegerField()
    sold=models.IntegerField()
