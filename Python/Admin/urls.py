from django.urls import path,include
from Admin import views
urlpatterns = [
    path('add/',views.add),
    path('larger/',views.larger),
    path('calc/',views.calc),
    path('salary/',views.salary),
    path('district/',views.district),
    
]   