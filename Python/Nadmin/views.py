from django.shortcuts import render,redirect
from Nadmin.models import *
from Guest.models import *
from User.models import *
from datetime import date
# Create your views here.

#Home Page
def LoadingHomePage(request):
    return render(request,"Nadmin/HomePage.html")

#District

def districtInsertSelect(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Nadmin/District.html",{'data':data})
    else:
        return render(request,"Nadmin/District.html",{'data':data})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Nadmin:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Nadmin:districtInsertSelect")
    else:
        return render(request,"Nadmin\District.html",{"editdata":editdata})
    

#Category

def categoryInsertSelect(request):
    data=tbl_category.objects.all()
    if request.method == "POST":
        CategoryName=request.POST.get('categoryname')
        tbl_category.objects.create(category_name=CategoryName)
        return render(request,"Nadmin/Category.html",{"data":data})
    else:
        return render(request,"Nadmin/Category.html",{"data":data})
    
def delCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('Nadmin:categoryInsertSelect')

def categoryupdate(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method == "POST":
        editdata.category_name=request.POST.get("categoryname")
        editdata.save()
        return redirect("Nadmin:categoryInsertSelect")
    else:
        return render(request,"Nadmin\Category.html",{"editdata":editdata})
    

#Admin

def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method == "POST":
        tbl_admin.objects.create(admin_name=request.POST.get("adminname"),admin_email=request.POST.get("adminemail"),admin_password=request.POST.get("adminpassword"))
        return render(request,"Nadmin/Admin.html",{"data":data})
    else:
        return render(request,"Nadmin/Admin.html",{"data":data})
    
def delAdmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect('Nadmin:adminInsertSelect')

def adminUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method == "POST":
        editdata.admin_name=request.POST.get("adminname")
        editdata.admin_email=request.POST.get("adminemail")
        editdata.admin_password=request.POST.get("adminpassword")
        editdata.save()
        return redirect("Nadmin:adminInsertSelect")
    else:
        return render(request,"Nadmin\Admin.html",{"editdata":editdata})
    
#Place

def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        data = tbl_place.objects.all()
        return render(request,"Nadmin/Place.html",{'data':data})
    else:
        return render(request,"Nadmin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Nadmin:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("Nadmin:placeInsertSelect")
    else:
        return render(request,"Nadmin\Place.html",{"editdata":editdata,"districtdata":district})

#SubCategory
    
def subcatInsertSelect(request):
    category=tbl_category.objects.all()
    data=tbl_subcat.objects.all()
    if request.method=="POST":
        subcat=request.POST.get('subcat')
        cat = tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcat.objects.create(subcat_name=subcat,category=cat)
        return render(request,"Nadmin/SubCategory.html",{'data':data})
    else:
        return render(request,"Nadmin/SubCategory.html",{'data':data,"catdata":category})

def delSubcat(request,did):
    tbl_subcat.objects.get(id=did).delete()
    return redirect("Nadmin:subcatInsertSelect")


#Department

def departmentInsertSelect(request):
    data=tbl_department.objects.all()
    if request.method == "POST":
        tbl_department.objects.create(department_name=request.POST.get("departmentname"))
        return render(request,"Nadmin/Department.html",{"data":data})
    else:
        return render(request,"Nadmin/Department.html",{"data":data})
    
def delDepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect('Nadmin:departmentInsertSelect')
        
def departmentupdate(request,eid):
    editdata=tbl_department.objects.get(id=eid)
    if request.method == "POST":
        editdata.department_name=request.POST.get("departmentname")
        editdata.save()
        return redirect("Nadmin:departmentInsertSelect")
    else:
        return render(request,"Nadmin\Department.html",{"editdata":editdata})
    
#Designation
    
def designationInsertSelect(request):
    data=tbl_designation.objects.all()
    if request.method == "POST":
        tbl_designation.objects.create(designation_name=request.POST.get("designationname"))
        return render(request,"Nadmin/Designation.html",{"data":data})
    else:
        return render(request,"Nadmin/Designation.html",{"data":data})
    
def delDesignation(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect('Nadmin:designationInsertSelect')
        
def designationupdate(request,eid):
    editdata=tbl_designation.objects.get(id=eid)
    if request.method == "POST":
        editdata.designation_name=request.POST.get("designationname")
        editdata.save()
        return redirect("Nadmin:designationInsertSelect")
    else:
        return render(request,"Nadmin\Designation.html",{"editdata":editdata})
    
#Employee
    
def employeeInsertSelect(request):
    department = tbl_department.objects.all()
    designation = tbl_designation.objects.all()
    data=tbl_employee.objects.all()
    if request.method=="POST":
        dis = tbl_department.objects.get(id=request.POST.get('sel_department'))
        des = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        tbl_employee.objects.create(employee_name=request.POST.get("employeename"),employee_contact=request.POST.get("employeecontact"),employee_email=request.POST.get("employeeemail"),department=dis,designation=des)
        return render(request,"Nadmin/Employee.html",{'data':data})
    else:
        return render(request,"Nadmin/Employee.html",{'data':data,"departmentdata":department,"designationdata":designation})

def delEmployee(request,did):
    tbl_employee.objects.get(id=did).delete()
    return redirect("Nadmin:employeeInsertSelect")

def employeeupdate(request,eid):
    department = tbl_department.objects.all()
    designation = tbl_designation.objects.all()
    editdata=tbl_employee.objects.get(id=eid)
    if request.method=="POST":
        editdata.employee_name=request.POST.get("employeename")
        editdata.employee_contact=request.POST.get("employeecontact")
        editdata.employee_email=request.POST.get("employeeemail")
        dis = tbl_department.objects.get(id=request.POST.get('sel_department'))
        des = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        editdata.department = dis
        editdata.designation = des
        editdata.save()
        return redirect("Nadmin:employeeInsertSelect")
    else:
        return render(request,"Nadmin\Employee.html",{"editdata":editdata,"departmentdata":department,"designationdata":designation})

#View User

def ViewUser(request):
    data=tbl_user.objects.all()
    return render(request,"Nadmin/ViewUser.html",{'data':data})

def delUser(request,did):
    tbl_user.objects.get(id=did).delete()
    return redirect("Nadmin:ViewUser")

#View Merchant

def merchantListNew(request):
    merchantdata=tbl_merchant.objects.filter(merchant_status=0)
    return render(request,"Nadmin/MerchantListNew.html",{'data':merchantdata})

def acceptmerchant(request,aid):
    merchant = tbl_merchant.objects.get(id=aid)
    merchant.merchant_status=1
    merchant.save()
    return redirect("Nadmin:index")

def rejectmerchant(request,rid):
    merchant=tbl_merchant.objects.get(id=rid)
    merchant.merchant_status=2
    merchant.save()
    return redirect("Nadmin:index")

def merchantListAccepted(request):
    merchantdata = tbl_merchant.objects.filter(merchant_status=1)
    return render(request,"Nadmin/MerchantListAccepted.html",{"merchantdata":merchantdata})

def merchantListRejected(request):
    merchantdata = tbl_merchant.objects.filter(merchant_status=2)
    return render(request,"Nadmin/MerchantListRejected.html",{"merchantdata":merchantdata})   


#View User

def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Nadmin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("Nadmin:indexuser")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("Nadmin:indexuser")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Nadmin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Nadmin/UserListRejected.html",{"userdata":userdata})    




def my_pro(request):
    data=tbl_admin.objects.get(id=request.session["aid"])
    return render(request,"Nadmin/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_admin.objects.get(id=request.session["aid"])
    if request.method=="POST":
        prodata.admin_name=request.POST.get('txtname')
        prodata.admin_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Nadmin/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Nadmin/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_admin.objects.filter(id=request.session["uid"],admin_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                admindata=tbl_admin.objects.get(id=request.session["uid"],admin_password=request.POST.get('txtcurpass'))
                admindata.admin_password=request.POST.get('txtnewpass')
                admindata.save()
                return render(request,"Nadmin/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Nadmin/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Nadmin/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Nadmin/ChangePassword.html")
    

def UserComplaintListNew(request):
    data=tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"Nadmin/UserComplaintListNew.html",{'data':data})

def UserComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("Nadmin:index")
    else:
        return render(request,"Nadmin/index.html",{'complaint':complaint})
    

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Nadmin/UserFeedbackNew.html",{'data':data})

def ViewFeedback(request,fid):
    feedback = tbl_feedback.objects.get(id=fid)
    feedback.feedback_status = 1
    feedback.save()
    return redirect("Nadmin:index")

def UserComplaintSolved(request):
    complaint = tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Nadmin/UserComplaintSolved.html",{"complaint":complaint})


def ViewAds(request):
    data=tbl_ad.objects.all()
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"Nadmin/ViewAds.html",{'data':data,"merchant": merchant})

def delAds(request,adid):
    tbl_ad.objects.get(id=adid).delete()
    return redirect("Nadmin:ViewAds")


def ViewAdsMore(request, adid):
    ad = tbl_ad.objects.get(id=adid)
    reviews = ad.tbl_review_set.all()
    user_id = request.session.get('uid')
    # user_reviews = tbl_review.objects.filter(user_id=user_id, ad=ad)
    
    return render(request, "Nadmin/ViewAdsMore.html", {'ad': ad,'reviews': reviews,"userid":user_id})

def delReview(request, did):
        review = tbl_review.objects.get(id=did)
        adid = review.ad.id
        review.delete()
        return redirect("Merchant:ViewAdsMore", adid=adid)

def ViewEvents(request):
    data=tbl_event.objects.all()
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"Nadmin/ViewEvents.html",{'data':data,"merchant": merchant})

def ViewEventsMore(request,eventid):
    data=tbl_event.objects.get(id=eventid)
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"Nadmin/ViewEventsMore.html",{'data':data,"merchant": merchant})

def delEvent(request,did):
    tbl_event.objects.get(id=did).delete()
    return redirect("Nadmin:ViewEvents")  

def index(request):
    merchantdata=tbl_merchant.objects.filter(merchant_status=0)
    merchant = tbl_merchant.objects.filter(merchant_status=1)
    merchants = tbl_merchant.objects.filter(merchant_status=2)
    registeredmerchants = tbl_merchant.objects.filter()
    eventdata =tbl_event.objects.all()
    addata=tbl_event.objects.all()
    admin_id = request.session.get("aid")
    admin = tbl_admin.objects.get(id=admin_id)
    admin_name = admin.admin_name
    complaints = tbl_complaint.objects.filter(complaint_status=0)
    complaints_with_user_names = {
        complaint.id: complaint.user.user_name for complaint in complaints
    }
    feedbacks = tbl_feedback.objects.filter(feedback_status=0)
    # Fetching users for the feedbacks
    feedbacks_with_user_names = {
        feedback.id: feedback.user.user_name if feedback.user else None for feedback in feedbacks
    }

    # Fetching merchants for the feedbacks
    feedbacks_with_merchant_names = {
        feedback.id: feedback.merchant.merchant_name if feedback.merchant else None for feedback in feedbacks
    }


    context = {
        'data': merchantdata,
        'merchant': merchant,
        'registeredmerchants': registeredmerchants,
        'merchants': merchants,
        'admin_name': admin_name,
        'eventdata': eventdata,
        'addata': addata,
        'complaints': complaints,
        'complaints_with_user_names': complaints_with_user_names,
        'feedbacks': feedbacks,
        'feedbacks_with_user_names': feedbacks_with_user_names,
        'feedbacks_with_merchant_names': feedbacks_with_merchant_names,
    }
    return render(request, "Nadmin/index.html", context)

def indexuser(request):
    userdata=tbl_user.objects.filter(user_status=0)
    user = tbl_user.objects.filter(user_status=1)
    users = tbl_user.objects.filter(user_status=2)
    registereduser = tbl_user.objects.filter()
    eventdata =tbl_event.objects.all()
    admin_id = request.session.get("aid")
    admin = tbl_admin.objects.get(id=admin_id)
    admin_name = admin.admin_name
    complaints = tbl_complaint.objects.filter(complaint_status=0)
    complaints_with_user_names = {
        complaint.id: complaint.user.user_name for complaint in complaints
    }
    feedbacks = tbl_feedback.objects.filter(feedback_status=0)
    # Fetching users for the feedbacks
    feedbacks_with_user_names = {
        feedback.id: feedback.user.user_name if feedback.user else None for feedback in feedbacks
    }

    # Fetching merchants for the feedbacks
    feedbacks_with_merchant_names = {
        feedback.id: feedback.merchant.merchant_name if feedback.merchant else None for feedback in feedbacks
    }


    context = {
        'data': userdata,
        'user': user,
        'users': users,
        'admin_name': admin_name,
        'registereduser': registereduser,
        'eventdata': eventdata,
        'complaints': complaints,
        'complaints_with_user_names': complaints_with_user_names,
        'feedbacks': feedbacks,
        'feedbacks_with_user_names': feedbacks_with_user_names,
        'feedbacks_with_merchant_names': feedbacks_with_merchant_names,
    }
    return render(request, "Nadmin/indexuser.html", context)