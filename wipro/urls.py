from django.contrib import admin
from django.urls import path
from.import views
from.views import articleAPIview
urlpatterns = [
    path('hello',views.hello,name="hello"),
    path('form',views.form,name="form"),
    path('table',views.table,name="table"),
    path('branchinfo',views.branchinfo,name="branchinfo"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('form1',views.form1,name="form1"),
    path('table1',views.table1,name="table1"),
    path('salooninfo',views.salooninfo,name="salooninfo"),
    path('edit1/<int:id>',views.edit1,name="edit1"),
    path('update1/<int:id>',views.update1,name="update1"),
    path('delete1/<int:id>',views.delete1,name="delete1"),
    path('form2',views.form2,name="form2"),
    path('table2',views.table2,name="table2"),
    path('serviceinfo',views.serviceinfo,name="serviceinfo"),
    path('edit2/<int:id>',views.edit2,name="edit2"),
    path('update2/<int:id>',views.update2,name="update2"),
    path('delete2/<int:id>',views.delete2,name="delete2"),
    path('regg',views.regg,name="regg"),
    path('cont',views.cont,name="cont"),
    path('req',views.req,name="req"),
    path('approve/<int:id>',views.approve,name="approve"),
    path('declined/<int:id>',views.declined,name="declined"),
    path('apr',views.apr,name="apr"),
    path('dec',views.dec,name="dec"),
    path('article_list',views.article_list,name="article_list"),
    path('article_detail/<int:pk>',views.article_detail,name="article_detail"),
    path('articleAPIview', views.articleAPIview.as_view(), name='article_api'),
    path('articledetails/<int:id>',views.articledetails.as_view(),name="articledetails"),
    
]