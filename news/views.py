from django.http import HttpResponse
from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Article
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Moringa Tribune')

   

def news_of_the_day(request):
    date = dt.date.today()
    html = f'''
    <html>
        <body>
            <h1> {date.day}-{date.month}-{date.year}</h1>
        </body>
    </html>
        '''
    return HttpResponse(html)


def news_of_the_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})



def past_days_news(request,past_date):
    date = dt.datetime.strptime(past_date, '%y-%m-%d').date()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}.{date.month}.{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)


def past_days_news(request,past_date):
    try:
        date = dt.datetime.strptime(past_date, '%y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})


def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})


