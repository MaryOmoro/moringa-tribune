from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

class EditorTestClass(TestCase):
    
    
    def setUp(self):
        self.shallom = Editor(first_name = 'Shallom', last_name = 'Kim', email = 'kim@standard.com')
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.shallom,Editor))

    def test_save_method(self):
        self.shallom.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)



class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)


    def test_get_news_by_date(self):
        test_date = '2022-12-11'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)


        


