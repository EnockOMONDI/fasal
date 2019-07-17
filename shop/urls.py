from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'shop'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^beneficiaries/', views.product_list, name='product_list'),
    url(r'^media/', views.media_list, name='media_list'),
    url(r'^team_list/', views.team_list, name='team_list'),
    url(r'^contact/', views.contact, name='contact'),  
    url(r'^donate/', views.donate, name='donate'), 
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
   
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
