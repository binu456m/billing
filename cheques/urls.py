from django.conf.urls import url, include
from django.contrib import admin
import views
from django.views import generic


urlpatterns = [               
    
    url(r'^create-cheque-details/$',views.create_cheque,name='create_cheque'),
    url(r'^view-cheques-details/$',views.view_cheques,name='view_cheques'),
    url(r'^edit-cheque-details/(?P<pk>.*)/$',views.edit_cheque,name='edit_cheque'),
    url(r'^view-cheque-details/(?P<pk>.*)/$',views.view_cheque,name='view_cheque'),
    url(r'^delete-cheque-details/(?P<pk>.*)/$',views.delete_cheque,name='delete_cheque'),
]