from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^today/$',views.news_of_the_day,name = 'newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})$', views.past_days_news, name = 'pastNews'),
]
