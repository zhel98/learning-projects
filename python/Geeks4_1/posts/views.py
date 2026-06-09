from django.shortcuts import render
from django.http.response import HttpResponse
from posts.models import Post, Category
# Create your views here.

def hello_world(request):
    
    return HttpResponse("<h1>hello world!</h1>")


def about(request):
    
    return render(request, 'about.html')


def posts_list(request):
    posts = Post.objects.all()
    
    text = ''
    
    for post in posts:
        text+=f'<h1>{post.title}</h1><br>{post.content}<br>'
    
    return HttpResponse(text)

def categories_list(request):
    categories = Category.objects.filter(is_active=True)

    text = ''

    for category in categories:
        text += f'<h1>{category.title}</h1><p>{category.description}</p><br>'

    return HttpResponse(content=text)
    