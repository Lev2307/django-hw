from django.shortcuts import render
from django.http import HttpResponse, Http404
from news.models import News
# Create your views here.

def index(request, *args, **kwargs):
    qs = News.objects.all()
    context = {'news_list': qs}
    return render(request, 'index.html', context)

def detail_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except:
        raise Http404

    return HttpResponse(f'<h1>{obj.article}</h1>')
