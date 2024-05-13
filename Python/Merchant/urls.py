from django.urls import path
from Merchant import views
app_name="Merchant"
urlpatterns = [

#Home Page

    path('homepage/',views.homepage,name="homepage"),

#My Profile

    path('My_profile/',views.my_pro,name="my_pro"),

#Edit Profile

    path('editprofile/',views.editprofile,name="editprofile"),
    
#ChangePassword
    
    path('changepassword/',views.changepassword,name="changepassword"),


    path('MerchantFeedback/', views.MerchantFeedback, name='MerchantFeedback'),
    
    
    path('PostAds/', views.PostAds, name='PostAds'),
    path('delAd/<int:did>', views.delAd,name="delAd"),

    path('PostEvents/', views.PostEvents, name='PostEvents'),
    path('delEvent/<int:did>', views.delEvent,name="delEvent"),

    path('ViewAds/', views.ViewAds, name='ViewAds'),

    path('ViewAdsMore/<int:adid>/', views.ViewAdsMore, name='ViewAdsMore'),
    path('delReview/<int:did>', views.delReview,name="delReview"),

    path('Ajaxsubcategory/',views.Ajaxsubcategory,name="Ajaxsubcategory"),

    path('ViewEvents/', views.ViewEvents, name='ViewEvents'),
    path('ViewEventsMore/<int:eventid>', views.ViewEventsMore, name='ViewEventsMore'),

    path('index/',views.index,name="index"),

    path('users/',views.users,name="users"),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),


    path('jobs/', views.jobs, name='jobs'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('goods/', views.goods, name='goods'),
    path('services/', views.services, name='services'),
    path('community/', views.community, name='community'),
    path('vacationrentals/', views.vacationrentals, name='vacationrentals'),
    path('pets/', views.pets, name='pets'),
    path('business/', views.business, name='business'),
    path('realestate/', views.realestate, name='realestate'),

    path('user_profile/<int:id>/', views.user_profile, name='user_profile'),

]

