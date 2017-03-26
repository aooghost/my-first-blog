from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'news/index.html', {'posts': posts})

#def index(request):
#    posts = Post.objects.all()
#    iloscPostow = posts.count()
#    return render_to_response('news/index.html',{'iloscPostow': iloscPostow })
