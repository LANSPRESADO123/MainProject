from django.shortcuts import render,redirect
from Nadmin.models import *
from Guest.models import *
from django.http import HttpResponse
# Create your views here.

#UserRegistration

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userwait")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})

# def ajaxplace(request):
#     dis = tbl_district.objects.get(id=request.GET.get("did"))
#     place = tbl_place.objects.filter(district=dis)

#     # Build HTML string with place options (example using string concatenation)
#     place_options = ""
#     for p in place:
#         place_options += f"<option value='{p.id}'>{p.place_name}</option>"

#     # Return HTML string with content type text/html
#     return HttpResponse(place_options, content_type="text/html")


#MerchantRegistration

def merchantRegistration(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_merchant.objects.create(merchant_name=request.POST.get('merchantname'),merchant_contact=request.POST.get('merchantcontact'),
                                    merchant_gender=request.POST.get('merchantgender'),merchant_email=request.POST.get('merchantemail'),
                                    merchant_password=request.POST.get('merchantpassword'),merchant_shopname=request.POST.get('shopname'),
                                    merchant_photo=request.FILES.get("merchantimage"),merchant_address=request.POST.get('merchantaddress'),
                                    merchant_dob=request.POST.get('dob'),merchant_license=request.POST.get('merchantlicense'),place=plc)
        return redirect("Guest:merchantwait")
    else:
        return render(request,"Guest/NewMerchant.html",{"districtdata":district})
    

#Login
    
def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"),user_status=1).count()
        merchantcount = tbl_merchant.objects.filter(merchant_email=request.POST.get("txt_email"),merchant_password=request.POST.get("txt_password"),merchant_status=1).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:index")
        elif merchantcount >0:
            merchant = tbl_merchant.objects.get(merchant_email=request.POST.get("txt_email"),merchant_password=request.POST.get("txt_password"))
            request.session["mid"] = merchant.id
            request.session["mname"] = merchant.merchant_name
            return redirect("Merchant:index")
        elif admincount >0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("Nadmin:index")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")
    
def index(request):
    return render(request,"Guest/index.html")

def register(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_merchant.objects.create(merchant_name=request.POST.get('merchantname'),merchant_contact=request.POST.get('merchantcontact'),
                                    merchant_gender=request.POST.get('merchantgender'),merchant_email=request.POST.get('merchantemail'),
                                    merchant_password=request.POST.get('merchantpassword'),merchant_shopname=request.POST.get('shopname'),
                                    merchant_photo=request.FILES.get("merchantimage"),merchant_address=request.POST.get('merchantaddress'),
                                    merchant_dob=request.POST.get('dob'),merchant_license=request.POST.get('merchantlicense'),place=plc)
        return redirect("Guest:merchantwait")
    else:
        return render(request,"Guest/register.html",{"districtdata":district})
    
def merchantwait(request):
    return render(request,"Guest/merchantwait.html")
def userwait(request):
    return render(request,"Guest/userwait.html")
    