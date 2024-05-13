from django.db import models

# Create your models here.
from Guest.models import *
from Merchant.models import*
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    merchant = models.ForeignKey(tbl_merchant, on_delete=models.CASCADE, null=True)


class tbl_review(models.Model):
    review_rating=models.CharField(max_length=500)
    review_content=models.CharField(max_length=500)
    review_postdate=models.DateField(auto_now_add=True)
    review_posttime=models.TimeField(auto_now_add=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    merchant = models.ForeignKey(tbl_merchant, on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(tbl_ad, on_delete=models.CASCADE)


    