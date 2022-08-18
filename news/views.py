

from unicodedata import category
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import Http404
def index(request, slug=None):

    categories = Category.objects.all()
    if slug == None:
        news_all = News.objects.all().order_by('-created_date')
    else:
        print('__________')
        news_all = News.objects.filter(category=Category.objects.get(slug=slug)).order_by('-created_date')
        print(news_all)

        
    paginator = Paginator(news_all, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context = {
        'categories':categories,
        'news':news
    }

    return render(request=request, template_name='news/index.html', context=context)
    
def detail_post(request, slug= None):
    categories = Category.objects.all()
    try:
        liked_element = Like.objects.get(author=request.user, news=News.objects.get(slug=slug))
    except:
        liked_element=None
    if request.method =='GET' and request.GET.get('like'):
        if request.user.is_authenticated:
            post =News.objects.get(slug=slug)
            try:
                liked_el = Like.objects.get(author=request.user, news=News.objects.get(slug=slug))
                if liked_el:
                    print('____liked___')
                    if liked_el.like ==True:
                        print('___like_True__')
                        liked_el.like =False
                        liked_el.save()
                    else:
                        liked_el.delete()
            except:
                newlike=Like(news=post, author=request.user, like=True)
                newlike.save()


    if slug!=None:

        try:
            post = News.objects.get(slug=slug)
            likes = Like.objects.filter(news=post)
            context ={
                'post':post,
                'categories':categories,
                'liked_element':liked_element,
                'likes':likes

            }
            return render(request=request, template_name='news/detail_post.html', context=context)
        except:
            pass
    raise Http404
              