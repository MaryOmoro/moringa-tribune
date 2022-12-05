from django.urls import re_path as url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('news.urls')),
]