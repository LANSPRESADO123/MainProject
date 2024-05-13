from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [

#NewUser

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),

#NewMerchant

    path('NewMerchant/',views.merchantRegistration,name="merchantRegistration"),

#Login

    path('Login/',views.Login,name="Login"),



    path('index/',views.index,name="index"),

    path('register/',views.register,name="register"),

    path('merchantwait/',views.merchantwait,name="merchantwait"),
    path('userwait/',views.userwait,name="userwait"),
    
]
