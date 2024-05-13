from django.shortcuts import render,redirect
from Nadmin.models import *
from Guest.models import * 
from User.models import *
from Merchant.models import *
from datetime import datetime
from django.utils import timezone
from django.db.models import Q
from itertools import chain
from django import forms

# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")
    
    

#Complaint
    
def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")

def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("User:UserFeedback")
    else:
        return render(request,"User/UserFeedback.html",{"data":data})
    

def ViewAds(request):
    data=tbl_ad.objects.all()
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"User/ViewAds.html",{'data':data,"merchant": merchant})


def ViewEvents(request):
    data=tbl_event.objects.all()
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"User/ViewEvents.html",{'data':data,"merchant": merchant})

def ViewEventsMore(request,eventid):
    data=tbl_event.objects.get(id=eventid)
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"User/ViewEventsMore.html",{'data':data,"merchant": merchant})



def ViewAdsMore(request, adid):
    ad = tbl_ad.objects.get(id=adid)
    reviews = ad.tbl_review_set.all()
    user_id = request.session.get('uid')
    user_reviews = tbl_review.objects.filter(user_id=user_id, ad=ad) 
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user_id = request.session.get('uid')
        current_datetime = datetime.now()
        
        ad = tbl_ad.objects.get(id=adid)
        
        review = tbl_review.objects.create(
            review_rating=rating,
            review_content=comment,
            review_postdate=current_datetime.date(),
            review_posttime=current_datetime.time(),
            user_id=user_id,
            ad=ad 
        )
        return redirect('User:ViewAdsMore', adid=adid)
    
    
    return render(request, "User/ViewAdsMore.html", {'ad': ad,'reviews': reviews,"userid":user_id})

def delReview(request, did):
        review = tbl_review.objects.get(id=did)
        adid = review.ad.id
        review.delete()
        return redirect("User:ViewAdsMore", adid=adid)

def index(request):
    form = PlaceSelectorForm(request.GET)
    events = tbl_event.objects.all()
    ads = tbl_ad.objects.all()
    if form.is_valid():
        place = form.cleaned_data.get('place')
        if place:
            ads = ads.filter(place_id=8)
            events = events.filter(place=place)

    return render(request, "User/index.html", {
        'form': form,
        'ads': ads,
        'events': events
    })   

def merchants(request):
    merchantdata = tbl_merchant.objects.filter(merchant_status=1)
    return render(request,"User/merchants.html",{"merchantdata":merchantdata})


def chatpage(request,id):
    user  = tbl_merchant.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_user = tbl_merchant.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,merchant_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
        else:
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_user = tbl_merchant.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),user_from=from_user,merchant_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
    else:
        from_user = tbl_user.objects.get(id=request.session["uid"])
        to_user = tbl_merchant.objects.get(id=request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,merchant_to=to_user,chat_file="")
        return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(merchant_from=tid) | Q(merchant_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(merchant_to=request.GET.get("tid")) | (Q(merchant_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def merchant_profile(request, id):
    merchant = tbl_merchant.objects.get(id=id)
    return render(request, 'User/merchant_profile.html', {'merchant': merchant})

def jobs(request):
    full_time_jobs_ads = tbl_ad.objects.filter( subcat=9) 
    part_time_jobs_ads = tbl_ad.objects.filter( subcat=7) 
    contract_jobs_ads = tbl_ad.objects.filter( subcat=6) 
    internship_jobs_ads = tbl_ad.objects.filter( subcat=7) 
    remote_jobs_ads = tbl_ad.objects.filter( subcat=7) 
    combined_ads = list(chain(full_time_jobs_ads, part_time_jobs_ads,contract_jobs_ads,internship_jobs_ads,remote_jobs_ads))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'full_time_jobs_ads': full_time_jobs_ads,
        "part_time_jobs_ads": part_time_jobs_ads,
        "contract_jobs_ads": contract_jobs_ads,
        "internship_jobs_ads": internship_jobs_ads,
        "remote_jobs_ads": remote_jobs_ads,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
    }
    return render(request, "User/jobs.html", context)


def vehicles(request):
    cars = tbl_ad.objects.filter( subcat=21) 
    motorcycles = tbl_ad.objects.filter( subcat=22) 
    
    combined_ads = list(chain(cars, motorcycles))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'cars': cars,
        "motorcycles": motorcycles,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
    }
    return render(request, "User/vehicles.html", context)


def goods(request):
    electronics = tbl_ad.objects.filter( subcat=23) 
    furniture = tbl_ad.objects.filter( subcat=24) 
    clothing = tbl_ad.objects.filter( subcat=25) 
    collectibles = tbl_ad.objects.filter( subcat=26) 
    sporting = tbl_ad.objects.filter( subcat=27) 
    
    combined_ads = list(chain(electronics,furniture,clothing,collectibles,sporting))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'electronics': electronics,
        "furniture": furniture,
        "clothing": clothing,
        "collectibles": collectibles,
        "sporting": sporting,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
    }
    return render(request, "User/goods.html", context)


def services(request):
    home = tbl_ad.objects.filter( subcat=28) 
    landscaping = tbl_ad.objects.filter( subcat=29) 
    petcare = tbl_ad.objects.filter( subcat=30) 
    cleaning = tbl_ad.objects.filter( subcat=31) 
    event = tbl_ad.objects.filter( subcat=32) 
    
    combined_ads = list(chain(home,landscaping,petcare,cleaning,event))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'home': home,
        "landscaping": landscaping,
        "petcare": petcare,
        "cleaning": cleaning,
        "event": event,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
    }
    return render(request, "User/services.html", context)


def community(request):
    lostandfound = tbl_ad.objects.filter( subcat=33) 
     
    
    combined_ads = list(chain(lostandfound))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'lostandfound': lostandfound,
        "ads_with_subcat_names": ads_with_subcat_names,        
               
    }
    return render(request, "User/community.html", context)



def vacationrentals(request):
    houses = tbl_ad.objects.filter( subcat=41) 
    apartments = tbl_ad.objects.filter( subcat=42) 
    beachhouses = tbl_ad.objects.filter( subcat=43) 
     
    
    combined_ads = list(chain(houses,apartments,beachhouses))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'houses': houses,
        'apartments': apartments,
        'beachhouses': beachhouses,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
               
    }
    return render(request, "User/vacationrentals.html", context)



def pets(request):
    dogs = tbl_ad.objects.filter( subcat=36) 
    cats = tbl_ad.objects.filter( subcat=37) 
    birds = tbl_ad.objects.filter( subcat=38) 
    fish = tbl_ad.objects.filter( subcat=39) 
    other = tbl_ad.objects.filter( subcat=40) 
     
    
    combined_ads = list(chain(dogs,cats,birds,fish,other))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'dogs': dogs,
        'cats': cats,
        'birds': birds,
        'fish': fish,
        'other': other,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
               
    }
    return render(request, "User/pets.html", context)



def business(request):
    office = tbl_ad.objects.filter( subcat=34) 
     
    
    combined_ads = list(chain(office))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'office': office,
        "ads_with_subcat_names": ads_with_subcat_names,        
               
    }
    return render(request, "User/business.html", context)



def realestate(request):
    house_sale = tbl_ad.objects.filter( subcat=16) 
    house_rent = tbl_ad.objects.filter( subcat=17) 
    apartment = tbl_ad.objects.filter( subcat=18) 
    land = tbl_ad.objects.filter( subcat=20) 
     
    
    combined_ads = list(chain(house_sale,house_rent,apartment,land))
    ads_with_subcat_names = {
    ad.id: ad.subcat.subcat_name for ad in combined_ads
}
    context = {
        'house_sale': house_sale,
        'house_rent': house_rent,
        'apartment': apartment,
        'land': land,
        "ads_with_subcat_names": ads_with_subcat_names,        
        "combined_ads": combined_ads,        
               
    }
    return render(request, "User/realestate.html", context)

class PlaceChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Return a string that will be used as the label for this object in the dropdown
        return obj.place_name

class PlaceSelectorForm(forms.Form):
    place = PlaceChoiceField(
        queryset=tbl_place.objects.all(),
        label="Select a place",
        empty_label="All Listed places",
        required=False,
        to_field_name="place_name",
    )