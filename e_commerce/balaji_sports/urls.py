from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='home'),
    path('MasterKits.html',Master,name="master"),
    path('SimpleKits.html',Simple,name="Simple"),
    path('about.html',AboutUs,name='AboutUS'),
    path('contact/',ContactUS,name='ContactUS'),
    path('tracker/',TrackingStatus,name='TrackingStatus'),
    path('search/',Search,name='Search'),
    path('productview/<int:prodid>',ProductView,name='ProductView'),
    path('checkout/',Checkout,name='Checkout'),
    path('cart/',Cart,name='Cart'),
    path('login/',login,name='login'),
    path('update_item/',updateitem,name='update_item'),
    path('',include("accounts.urls"))
]

urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)