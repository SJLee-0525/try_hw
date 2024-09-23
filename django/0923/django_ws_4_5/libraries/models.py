from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    author = models.TextField()
    title = models.TextField()
    publisher = models.CharField(max_length=100)
    fixed_price = models.BooleanField(default=False)
    pub_date = models.DateField()
    link = models.URLField()
    adult = models.BooleanField()

    @classmethod
    def insert_data(cls):
        API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
        API_KEY = 'ttbsungjoon1111015001'

        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewSpecial',
            'MaxResults': '20',
            'start': '1',
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
        }

        response = requests.get(API_URL, params=params).json()

        for item in response['item']:
            my_model = cls(
                isbn=item['isbn'], 
                isbn13=item['isbn13'],
                author=item['author'],
                title=item['title'],
                pub_date=item['pubDate'],
                link=item['link'],
                fixed_price=item['fixedPrice'],
                publisher=item['publisher'],
                adult=item['adult'],
                )
            my_model.save()
    
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

   

    # @classmethod
    # def insert_data(cls):
    #     response = requests.get('https://api.example.com/data')
    #     data = response.json()

    #     for item in data:
    #         my_model = cls(field1=item['field1'], field2=item['field2'])
    #         my_model.save()

# django shell에서 아래 코드 실행
# MyModel.insert_data()