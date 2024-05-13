from django.db import models

# Create your models here.
from Nadmin.models import *
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
    
    
#New Merchant
    
class tbl_merchant(models.Model):
    merchant_name=models.CharField(max_length=30)
    merchant_contact=models.CharField(max_length=30)
    merchant_gender=models.CharField(max_length=30)
    merchant_email=models.CharField(max_length=30)
    merchant_password=models.CharField(max_length=30)
    merchant_shopname=models.CharField(max_length=30)
    merchant_license=models.CharField(max_length=8)
    merchant_address=models.CharField(max_length=50)
    merchant_dob=models.CharField(max_length=30)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    merchant_photo = models.FileField(upload_to='Assets/UserPhoto/')
    merchant_status = models.IntegerField(default="0")
    

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    merchant_from = models.ForeignKey(tbl_merchant,on_delete=models.CASCADE,related_name="merchant_from",null=True)
    merchant_to = models.ForeignKey(tbl_merchant,on_delete=models.CASCADE,related_name="merchant_to",null=True)