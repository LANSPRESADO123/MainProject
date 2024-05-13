from django.shortcuts import render,redirect
from Nadmin.models import *
from Guest.models import *
from User.models import *
from Merchant.models import *
from datetime import datetime
from django.db.models import Q
from itertools import chain

# Create your views here.

def homepage(request):
    return render(request,"Merchant/HomePage.html")

def my_pro(request):
    data=tbl_merchant.objects.get(id=request.session["mid"])
    return render(request,"Merchant/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_merchant.objects.get(id=request.session["mid"])
    if request.method=="POST":
        prodata.merchant_name=request.POST.get('txtname')
        prodata.merchant_contact=request.POST.get('txtcon')
        prodata.merchant_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Merchant/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Merchant/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_merchant.objects.filter(id=request.session["mid"],merchant_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                merchantdata=tbl_merchant.objects.get(id=request.session["uid"],merchant_password=request.POST.get('txtcurpass'))
                merchantdata.user_password=request.POST.get('txtnewpass')
                merchantdata.save()
                return render(request,"Merchant/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Merchant/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Merchant/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Merchant/ChangePassword.html")


def MerchantFeedback(request):
    data=tbl_feedback.objects.filter(merchant=request.session["mid"])
    merchantID=tbl_merchant.objects.get(id=request.session["mid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,merchant=merchantID)
        return redirect("Merchant:MerchantFeedback")
    else:
        return render(request,"Merchant/MerchantFeedback.html",{"data":data})
    

def PostAds(request):
    data=tbl_ad.objects.filter(merchant=request.session["mid"])
    merchantID=tbl_merchant.objects.get(id=request.session["mid"])
    district=tbl_district.objects.all()
    category=tbl_category.objects.all()
    if request.method=="POST":
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        subcat=tbl_subcat.objects.get(id=request.POST.get('sel_subcat'))
        title=request.POST.get('adtitle')
        description=request.POST.get('addescription')
        image=request.FILES.get("adimage")
        tbl_ad.objects.create(ad_title=title,ad_description=description,ad_image=image,merchant=merchantID,place=plc ,subcat=subcat)
        return redirect("Merchant:PostAds")
    else:
        return render(request,"Merchant/PostAds.html",{"data":data,"districtdata":district,"categorydata":category})
    
def delAd(request,did):
    tbl_ad.objects.get(id=did).delete()
    return redirect("Merchant:PostAds")    


def PostEvents(request):
    data=tbl_event.objects.filter(merchant=request.session["mid"])
    merchantID=tbl_merchant.objects.get(id=request.session["mid"])
    district=tbl_district.objects.all()
    category=tbl_category.objects.all()
    if request.method=="POST":
        plc=tbl_place.objects.get(id=request.POST.get('sel_place'))
        subcat=tbl_subcat.objects.get(id=request.POST.get('sel_subcat'))
        title=request.POST.get('eventtitle')
        description=request.POST.get('eventdescription')
        image=request.FILES.get("eventimage")
        fromdate=request.POST.get('eventfromdate')
        todate=request.POST.get('eventtodate')
        time=request.POST.get('eventtime')
        loc=request.POST.get('eventlocation')
        tbl_event.objects.create(event_title=title,event_description=description,event_image=image,event_fromdate=fromdate,event_todate=todate,event_time=time,event_location=loc,merchant=merchantID,place=plc,subcat=subcat)
        return redirect("Merchant:PostEvents")
    else:
        return render(request,"Merchant/PostEvents.html",{"data":data,"districtdata":district,"categorydata":category})
    
def delEvent(request,did):
    tbl_event.objects.get(id=did).delete()
    return redirect("Merchant:PostEvents")   

def ViewAds(request):
    data=tbl_ad.objects.all()
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.filter(id=merchant_id)
    return render(request,"Merchant/ViewAds.html",{'data':data,"merchant": merchant}) 


def ViewAdsMore(request, adid):
    ad = tbl_ad.objects.get(id=adid)
    reviews = ad.tbl_review_set.all()
    user_id = request.session.get('uid')
    user_reviews = tbl_review.objects.filter(user_id=user_id, ad=ad) 
    is_author = {review.id: True for review in user_reviews}
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
        return redirect('Merchant:ViewAdsMore', adid=adid)
    
    
    return render(request, "Merchant/ViewAdsMore.html", {'ad': ad,'reviews': reviews,'is_author': is_author})

def delReview(request, did):
        review = tbl_review.objects.get(id=did)
        adid = review.ad.id  
        review.delete()
        return redirect("Merchant:ViewAdsMore", adid=adid)


def Ajaxsubcategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcat = tbl_subcat.objects.filter(category=cat)
    return render(request,"Merchant/Ajaxsubcategory.html",{"subcatdata":subcat})


def ViewEvents(request):
    data=tbl_event.objects.all()
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.filter(id=merchant_id)
    return render(request,"Merchant/ViewEvents.html",{'data':data,"merchant": merchant})

def ViewEventsMore(request,eventid):
    data=tbl_event.objects.get(id=eventid)
    merchant_id = request.session.get("mid")
    merchant = tbl_merchant.objects.get(id=merchant_id)
    return render(request,"Merchant/ViewEventsMore.html",{'data':data,"merchant": merchant})

def index(request):
    events = tbl_event.objects.all()
    ads = tbl_ad.objects.all()
    return render(request,"Merchant/index.html",{'events': events,'ads':ads})

def users(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Merchant/users.html",{"userdata":userdata})


def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Merchant/Chat.html",{"user":user})

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_merchant.objects.get(id=request.session["mid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),merchant_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Merchant/Chat.html")
        else:
            from_user = tbl_merchant.objects.get(id=request.session["mid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),merchant_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Merchant/Chat.html")
    else:
        from_user = tbl_merchant.objects.get(id=request.session["mid"])
        to_user = tbl_user.objects.get(id=request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),merchant_from=from_user,user_to=to_user,chat_file="")
        return render(request,"Merchant/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_merchant.objects.get(id=request.session["mid"])
    chat_data = tbl_chat.objects.filter((Q(merchant_from=user) | Q(merchant_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Merchant/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(merchant_from=request.session["mid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(merchant_to=request.session["mid"]))).delete()
    return render(request,"Merchant/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})



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
    return render(request, "Merchant/jobs.html", context)


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
    return render(request, "Merchant/vehicles.html", context)


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
    return render(request, "Merchant/goods.html", context)


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
    return render(request, "Merchant/services.html", context)


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
    return render(request, "Merchant/community.html", context)



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
    return render(request, "Merchant/vacationrentals.html", context)



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
    return render(request, "Merchant/pets.html", context)



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
    return render(request, "Merchant/business.html", context)



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
    return render(request, "Merchant/realestate.html", context)

def user_profile(request, id):
    user = tbl_user.objects.get(id=id)
    return render(request, 'Merchant/user_profile.html', {'user': user})

