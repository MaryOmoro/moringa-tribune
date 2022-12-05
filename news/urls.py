from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),
]
urlpatterns = [
    url('^today/$',views.news_of_the_day,name = 'newsToday')
]
urlpatterns = [
    url(r'^archives/(\d{4}-\d{2}-\d{2})$', views.past_days_news, name = 'pastNews')
]