from email.mime import base

import requests
from bs4 import BeautifulSoup

base_url = "https://medium.com"

def get_articles(tag):
    
    # get the inforamtion of avialable articles for the given tag
    url = "https://medium.com/tag/"+tag.lower() + "/latest"
    medium_data = requests.get(url)

    soup = BeautifulSoup(medium_data.text, 'html.parser')

    articles = soup.find_all('article')
    number_of_article = len(articles)

    fetched_data = []
    number=0
    for article in articles:

        # iterate on all the articles to fetch information
        creater_name = article.find('div',{'class':'o ao ji'}).find('p').text
        created_at = article.find('div',{'class':'o ao'}).find('p').text
        title = article.find('div',{'class':'l'}).find('h2').text
        blog_url =(article.find('a',{ 'aria-label':'Post Preview Title'}).get('href'))

        blog = {
            "creater_name":creater_name,
            "created_at": created_at[1:],
            "title":title,
            "number":str(number)+ '_' +tag
        } 
        fetched_data.append(blog)
        number=number+1   

    return fetched_data, number_of_article

def find_url(tag,n):
    
    # find url of an article
    urls = []
    url = "https://medium.com/tag/"+ tag.lower() + "/latest"
    medium_data = requests.get(url)

    soup = BeautifulSoup(medium_data.text, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        blog_url =(article.find('a',{ 'aria-label':'Post Preview Title'}).get('href'))
        urls.append(blog_url)
    
    return base_url+urls[int(n)]

def find_article_content(url):

    #find all the availabel content of an article
    information  = requests.get(url)
    soup = BeautifulSoup(information.text, 'html.parser')

    section = soup.find('section')
    paras = section.find_all('p')
    content = ""
    for para in paras:
        content += para.text

    title = soup.find('h1', {'class':'pw-post-title'}).text
    created_by = soup.find('div', {'class':'pw-author'}).find('a').text
    created_at = soup.find('p',{'class':'pw-published-date'}).text
    time = soup.find('div', {'class':'pw-reading-time'}).text

    article_content = {
        "title":title,
        "content":content,
        "created_by": created_by,
        "created_at" : created_at,
        "time": time
    }

    return article_content

def find_similar_tags(tag):

    # find the similar tags if requested not found
    similar_words = []
    url = "https://api.datamuse.com/words?ml=" + tag
    response = requests.get(url=url)
    response_data = response.json()
    for word in response_data:
        similar_words.append(word.get("word"))

    if len(similar_words) < 5:
        url = "https://api.datamuse.com/sug?s=" +tag
        response = requests.get(url=url)
        response_data = response.json()
        for word in response_data:
            similar_words.append(word.get("word"))
            
    return similar_words






    



