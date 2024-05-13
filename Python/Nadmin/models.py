from django.db import models


# Create your models here.

#District

class tbl_district(models.Model):
    district_name=models.CharField(max_length=20)

#Category

class tbl_category(models.Model):
    category_name=models.CharField(max_length=20)

#Admin
 
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_email=models.CharField(max_length=20)
    admin_password=models.CharField(max_length=20)

#Location

# class tb_location(models.Model):
#     location_name=models.CharField(max_length=20)
#     location_pin=models.CharField(max_length=20)

#Place

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

#SubCategory

class tbl_subcat(models.Model):
    subcat_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)


#Department
    
class tbl_department(models.Model):
    department_name=models.CharField(max_length=30)

#Designation
    
class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=30)

#Employee
    
class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=30)
    employee_contact=models.CharField(max_length=30)
    employee_email=models.CharField(max_length=30)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    designation=models.ForeignKey(tbl_designation,on_delete=models.CASCADE)




    