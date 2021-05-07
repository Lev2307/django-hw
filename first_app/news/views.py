from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse

from .forms import NewsModelForm, NewsForm, CommentaryModelForm
from .forms import NewsForm
from news.models import News, Commentaries

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
def create_view(request, *args, **kwargs):
    form = NewsModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        News.objects.create(**data)
    return render(request, 'forms.html', context)

@login_required
@permission_required('user.is_staff')
def edit_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = NewsModelForm(request.POST, instance=obj)
        if form.is_valid():
            edited_obj = form.save(commit=False)
            edited_obj.save()
    else:
        form = NewsModelForm(instance=obj)

    return render(request, 'edit_news_form.html', {'single_object': obj, 'form': form})

@login_required
@permission_required('user.is_staff')
def delete_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404
    obj.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def commentary_view(request, pk):
    form = CommentaryModelForm(request.POST or None)
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404

    if form.is_valid():
        text = form.cleaned_data.get('text')
        user = request.user
        commentary_obj = Commentaries(user=user, text=text)
        commentary_obj.save()
        obj.commentary.add(commentary_obj)
        obj.save()
        return redirect(f'/id/{pk}')
    return render(request, 'news/commentary.html', {'single_object': obj, 'form': form})
