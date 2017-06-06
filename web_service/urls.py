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
    url(r'search_Drugs_dict_test/$',views.search_Drugs_dict_test, name = 'search_Drugs_dict_test'),

    url(r'search_Drugs_alias/$',views.search_Drugs_alias, name = 'search_Drugs_alias'),
    url(r'search_Drugs_dict/$', views.search_Drugs_dict, name = 'search_Drugs_dict'),

    url(r'search_medical_alias/$',views.medical_test_index_alias_dict, name = 'search_medical_alias'),
    url(r'search_medical_dict/$',views.medical_test_index_dict, name = 'search_medical_dict'),
]
if settings.DEBUG is False:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT}),
    ]

