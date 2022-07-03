from django.shortcuts import render
from django.http import HttpResponse
from crawler.functions import *


def home(request):
    if request.method == "POST":
        tag = request.POST["tag"]
        fetched_data, number_of_articles = get_articles(tag)
        if number_of_articles == 0:
            similar_tags = find_similar_tags(tag)
            no_response = {
                "similar_tags":similar_tags,
                "message": "No article found for this tag, you can try with similar tags"
            }
            print(no_response.get('similar_tags'))
            return render(request, "crawler/home.html", context={"no_response":no_response})

        return render(request,"crawler/articles.html",context={"fetched_data":fetched_data})

    return render(request, "crawler/home.html")

def find_blog(request,number):
    print(number)

    n = number.split('_')[0]
    tag = number.split('_')[1]
    print(n, tag)
    url = find_url(tag ,n)
    print(url)
    article_content = find_article_content(url)
    print(article_content)
    return render(request,"crawler/article_information.html", context={"article_content": article_content})




# Create your views here.
