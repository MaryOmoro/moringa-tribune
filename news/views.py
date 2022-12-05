from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Moringa Tribune')

    import datetime as dt
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


def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday"]
    day = days[day_number]
    return day


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
    
    from django.http import HttpResponse, Http404
    def past_days_news(request,past_date):
        try:
            date = dt.datetime.strptime(past_date, '%y-%m-%d').date()
        except ValueError:
            raise Http404()

from django.shortcuts import render
    def welcome(request):
        return render(request, 'welcome.html')



