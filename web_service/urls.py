from django.conf.urls import  include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^index/$',views.index, name = 'index'),
    url(r'^search_hospital/$',views.search_hospital, name = 'search_hospital'),
    url(r'search_hospital_dict/$',views.search_hospital_dict, name = 'search_hospital_dict'),

    url(r'search_disease/$',views.search_disease, name = 'search_disease'),
    url(r'search_disease_dict/$',views.search_disease_dict, name = 'search_disease_dict'),

    url(r'search_Drugs_alias/$',views.search_Drugs_alias, name = 'search_Drugs_alias'),
    url(r'search_Drugs_dict/$', views.search_Drugs_dict, name = 'search_Drugs_dict'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)