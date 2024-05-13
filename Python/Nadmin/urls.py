from django.urls import path,include
from Nadmin import views

app_name="Nadmin"

urlpatterns = [

#Home Page
    
    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

#District

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),

#Category

    path('category/',views.categoryInsertSelect,name="categoryInsertSelect"),
    path('delCategory/<int:did>',views.delCategory,name="delCategory"),
    path('categoryupdate/<int:eid>',views.categoryupdate,name="categoryupdate"),

#Admin

    path('admin/',views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdmin/<int:did>',views.delAdmin,name="delAdmin"),
    path('adminUpdate/<int:eid>',views.adminUpdate,name="adminUpdate"),

#Place

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

#SubCategory

    path('subCategory/',views.subcatInsertSelect,name="subcatInsertSelect"),
    path('delSubcat/<int:did>',views.delSubcat,name="delSubcat"),

#Department

    path('department/',views.departmentInsertSelect,name="departmentInsertSelect"),
    path('delDepartment/<int:did>',views.delDepartment,name="delDepartment"),
    path('departmentupdate/<int:eid>',views.departmentupdate,name="departmentupdate"),

#Designation

    path('designation/',views.designationInsertSelect,name="designationInsertSelect"),
    path('delDesignation/<int:did>',views.delDesignation,name="delDesignation"),
    path('designationupdate/<int:eid>',views.designationupdate,name="designationupdate"),

#Employee

    path('Employee/', views.employeeInsertSelect,name="employeeInsertSelect"),
    path('delEmployee/<int:did>', views.delEmployee,name="delEmployee"),
    path('employeeupdate/<int:eid>',views.employeeupdate,name="employeeupdate"),


#View User

    path('ViewUser/',views.ViewUser,name="ViewUser"),
    path('delUser/<int:did>',views.delUser,name="delUser"),

#View Merchant
    path('MerchantListNew/',views.merchantListNew,name="merchantListNew"),
    path('acceptmerchant/<int:aid>',views.acceptmerchant,name="acceptmerchant"),
    path('rejectmerchant/<int:rid>',views.rejectmerchant,name="rejectmerchant"),
    path('MerchantListAccepted/',views.merchantListAccepted,name="merchantListAccepted"),
    path('MerchantListRejected/',views.merchantListRejected,name="merchantListRejected"),

#View User

    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),


    

#My Profile

    path('My_profile/',views.my_pro,name="my_pro"),

#Edit Profile

    path('editprofile/',views.editprofile,name="editprofile"),
    
#ChangePassword
    
    path('changepassword/',views.changepassword,name="changepassword"),



    path('UserComplaintListNew/',views.UserComplaintListNew,name="UserComplaintListNew"),
    path('UserComplaintReply/<int:cid>',views.UserComplaintReply,name="UserComplaintReply"),
    path('UserComplaintSolved/',views.UserComplaintSolved,name="UserComplaintSolved"),


    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),
    path('ViewFeedback/<int:fid>',views.ViewFeedback,name="ViewFeedback"),

    path('ViewAds/', views.ViewAds, name='ViewAds'),
    path('delAds/<int:adid>', views.delAds,name="delAds"),

    path('ViewAdsMore/<int:adid>/', views.ViewAdsMore, name='ViewAdsMore'),
    path('delReview/<int:did>', views.delReview,name="delReview"),

    path('ViewEvents/', views.ViewEvents, name='ViewEvents'),
    path('ViewEventsMore/<int:eventid>', views.ViewEventsMore, name='ViewEventsMore'),
    path('delEvent/<int:did>', views.delEvent,name="delEvent"),


    path('index/', views.index,name="index"),
    path('indexuser/', views.indexuser,name="indexuser"),

    # path('send-reply/<int:cid>/', views.UserComplaintReply, name='send_reply'),
]