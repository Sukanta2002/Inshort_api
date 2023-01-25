from bs4 import BeautifulSoup
import requests


def call(lan,category):
    newsFetchData = {
        'Sucess': True,
        'Category': category,
        'Language': lan,
        'data':[]
    }
    validLan =['hi','en']
    validCategory=['','national','business','sports','world','politics','technology','startup','entertainment','miscellaneous','hatke','science','automobile']
    if(lan not in  validLan):
        newsFetchData['Language']= 'Invalid Language'
        return newsFetchData

    if(category not in validCategory ):
        newsFetchData['Category']= 'Invalid Category'
        return newsFetchData
    try:
        html_page = requests.get(f'https://www.inshorts.com/{lan}/read/{category}').text
        soup = BeautifulSoup(html_page,'lxml').find('div',class_='card-stack')
        newss = soup.find_all('div',class_='news-card z-depth-1')
    except requests.exceptions.RequestException as e :
        newsFetchData['error'] = str(e)
        newsFetchData['Sucess'] = False
        return newsFetchData

    for news in newss:
        try:
            imageUrl = news.find('div',class_='news-card-image')['style'][23:-2] 
        except AttributeError:
            imageUrl = None 
        try:
            news_headline = news.find('span',itemprop="headline").text
        except AttributeError:
            news= None
        try:
            content = (news.find('div',itemprop="articleBody").text)
        except AttributeError:
             content = None
        try:
            readmore = news.find('a',class_='source').get('href')
        except AttributeError:
            readmore = None
        try:
            author = news.find('span',class_='author').text
        except AttributeError:
            author = None
        try:
            time = news.find('span',class_='time').text
        except AttributeError:
            time = None
        try:
            date = news.find('span',class_='date').text
        except AttributeError:
            date = None
       
        newsData ={
            'Titel':news_headline,
            'cotent':content,
            'Image Url':imageUrl,
            'Read More Url':readmore,
            'Author':author,
            'Time':time,
            'Date':date
        }

        newsFetchData['data'].append(newsData)

    return newsFetchData