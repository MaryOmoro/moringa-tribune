from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),
]
urlpatterns = [
    url('^today/$',views.news_of_the_day,name = 'newsToday')
]
