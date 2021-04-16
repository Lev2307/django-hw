from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, permission_required

from .forms import NewsModelForm
from .forms import NewsForm
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

    return render(request, 'news/detail.html', {'single_object': obj})

@login_required
@permission_required('user.is_staff', raise_exception=True)
def create_view(request, *args, **kwargs):
    form = NewsModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        News.objects.create(**data)
    return render(request, 'forms.html', context)