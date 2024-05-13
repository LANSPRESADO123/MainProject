from django.urls import path
from User import views
app_name="User"
urlpatterns = [

#Home Page

    path('homepage/',views.homepage,name="homepage"),

#My Profile

    path('My_profile/',views.my_pro,name="my_pro"),

    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint, name="POSTComplaint"),
    path('delComplaint/<int:did>', views.delComplaint,name="delComplaint"),


    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    
    path('ViewAds/', views.ViewAds, name='ViewAds'),

    path('ViewEvents/', views.ViewEvents, name='ViewEvents'),

    path('ViewAdsMore/<int:adid>/', views.ViewAdsMore, name='ViewAdsMore'),
    path('delReview/<int:did>', views.delReview,name="delReview"),

    path('ViewEventsMore/<int:eventid>', views.ViewEventsMore, name='ViewEventsMore'),

 
    path('index/',views.index,name="index"),

        path('merchants/',views.merchants,name="merchants"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('merchant_profile/<int:id>/', views.merchant_profile, name='merchant_profile'),

    path('jobs/', views.jobs, name='jobs'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('goods/', views.goods, name='goods'),
    path('services/', views.services, name='services'),
    path('community/', views.community, name='community'),
    path('vacationrentals/', views.vacationrentals, name='vacationrentals'),
    path('pets/', views.pets, name='pets'),
    path('business/', views.business, name='business'),
    path('realestate/', views.realestate, name='realestate'),

]