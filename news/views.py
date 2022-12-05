from django.http import HttpRespose

# Create your views here.
def welcome(request):
    return HttpRespose('Welcome to Moringa Tribune')

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
return HttpRespose(html)