from django.db import models
from Guest.models import *
# Create your models here.

class tbl_ad(models.Model):
    ad_title=models.CharField(max_length=500)
    ad_description=models.CharField(max_length=500)
    ad_image= models.FileField(upload_to='Assets/AdsImage/')
    merchant = models.ForeignKey(tbl_merchant, on_delete=models.CASCADE)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    subcat = models.ForeignKey(tbl_subcat, on_delete=models.CASCADE)
    


class tbl_event(models.Model):
    event_title=models.CharField(max_length=500)
    event_description=models.CharField(max_length=500)
    event_fromdate=models.DateField()
    event_todate=models.DateField()
    event_time=models.TimeField()
    event_status=models.IntegerField(default="0")
    event_location=models.CharField(max_length=500)
    event_image= models.FileField(upload_to='Assets/EventImage/')
    merchant = models.ForeignKey(tbl_merchant, on_delete=models.CASCADE)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    subcat = models.ForeignKey(tbl_subcat, on_delete=models.CASCADE)