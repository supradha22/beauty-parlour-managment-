from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.hey,name="hey"),
    path('contacts',views.contacts,name="contacts"),
    path('login',views.login,name="login"),
    path('contactinfo',views.contactinfo,name="contactinfo"),  
    path('register1',views.register1,name="register1"),
    path('registerinfo',views.registerinfo,name="registerinfo"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('publicdata',views.publicdata,name="publicdata"),
    path('card',views.card,name="card"),
    path('card1/<str:branch>',views.card1,name="card1"),
    path('card2/<str:saloon>',views.card2,name="card2"),
    path('view2/<int:id>',views.view2,name="view2"),
    path('bookinginfo/<int:id>',views.bookinginfo,name="bookinginfo"),
    path('bookservice/<int:id>',views.bookservice,name="bookservice"),
    path('history',views.history,name="history")
   
]
    