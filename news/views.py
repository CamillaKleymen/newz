from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsModel
from .NewsForm import NewsModel

<<<<<<< HEAD

=======
>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
def news_create(request):
    if request.method == 'POST':
        form = NewsModel(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsModel()
    return render(request, 'index.html', {'form': form})

<<<<<<< HEAD

=======
>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
def news_update(request, pk):
    news = get_object_or_404(NewsModel, pk=pk)
    if request.method == 'POST':
        form = NewsModel(request.POST, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsModel(instance=news)
    return render(request, 'index.html', {'form': form})

<<<<<<< HEAD

def news_list(request):
    news = NewsModel.objects.all()
    return render(request, 'index.html', {'news': news})


=======
def news_list(request):
    news = NewsModel.objects.all()
    return render(request, 'index.html', {'news': news})
>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
def news_detail(request, pk):
    news = get_object_or_404(NewsModel, pk=pk)
    return render(request, 'news_detail.html', {'news': news})

<<<<<<< HEAD

=======
>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
def news_delete(request, pk):
    news = get_object_or_404(NewsModel, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
<<<<<<< HEAD
    return render(request, 'index.html', {'news': news})
=======
    return render(request, 'index.html', {'news': news})
>>>>>>> 77ced790e329732b33d64c36c9ac7bb45d3f7198
