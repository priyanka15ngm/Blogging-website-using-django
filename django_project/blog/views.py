from django.shortcuts import render
# importing models.py so we can acess the data that we created in our database using queries instead of this dummy data
from .models import Post
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },

    {
        'author': 'PriyankaER',
        'title': 'Blog Post',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'


    }


]



def home(request):
    context = {
       'posts' : #  posts
                 Post.objects.all()

    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})


