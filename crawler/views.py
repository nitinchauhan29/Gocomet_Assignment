from operator import le
from django.shortcuts import render
from django.http import HttpResponse
from crawler.functions import *

frequent_searches = []
def home(request):
    if request.method == "POST":
        tag = request.POST["tag"]

        # get the number of articles available for the searched tag
        fetched_data, number_of_articles = get_articles(tag)

        if tag not in frequent_searches:
            frequent_searches.append(tag)

        if number_of_articles == 0:

            # if not found any relevant article for the given tag then show similar tags
            similar_tags = find_similar_tags(tag)
            no_response = {
                "similar_tags":similar_tags,
                "message": "No article found for this tag, you can try with similar tags"
            }
            print(no_response.get('similar_tags'))
            print(frequent_searches)
            return render(request, "crawler/home.html", context={"no_response":no_response, "search":frequent_searches})

        return render(request,"crawler/articles.html",context={"fetched_data":fetched_data})
    
    # if len(frequent_searches)>10:
    #     frequent_searches = frequent_searches[1:]

    print(frequent_searches)
    return render(request, "crawler/home.html", context={"search":frequent_searches})

def find_blog(request,number):

    # find content of blog 
    n = number.split('_')[0]
    tag = number.split('_')[1]
    print(n, tag)
    url = find_url(tag ,n)
    print(url)
    article_content = find_article_content(url)
    return render(request,"crawler/article_information.html", context={"article_content": article_content})

# Create your views here.
