
from django.conf.urls import url,include
from django.contrib import admin
from cfjapp.views import index,aboutus,ourStory,menu,order,location,shop,contact,shop_step_one,shop_step_three,shop_step_two,cf_login,cf_logout,cf_register,cf_test,register_yanzheng


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^index',index),
    url(r'^about',aboutus),
    url(r'^our_story',ourStory),
    url(r'^menu',menu),
    url(r'^shopping_cart_step_1',shop_step_one),
    url(r'^shopping_cart_step_2',shop_step_two),
    url(r'^shopping_cart_step_3',shop_step_three),
    url(r'^locations',location),
    url(r'^shop',shop),
    url(r'^contact',contact),
    url(r'^login',cf_login),
    url(r'^logout', cf_logout),
    url(r'^register', cf_register),
    url(r'^test',cf_test),
    url(r'^yanzheng',register_yanzheng),
]
