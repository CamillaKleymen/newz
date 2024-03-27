from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import NewsModel, CategoryModel, Cultural, National, TechScience,  WorldNews
from .forms import NewsForms

class HomePage(View):
    def get(self, request):
        categories = CategoryModel.objects.all()
        cultural = Cultural.objects.all()
        world = World.objects.all()
        national = National.objects.all()
        form = SearchForm()
        context = {'categories': categories, 'cultural': cultural, 'world': world, 'national': national, 'form': form}
        return render(request, 'tech-index.html', context)


class NewsCreateView(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'tech-index.html', {'form': form})

    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
        return render(request, 'tech-index.html', {'form': form})

class NewsUpdate(View):
    def get(self, request, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        form = NewsForm(instance=news)
        return render(request, 'tech-index.html', {'form': form})

    def post(self, request, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
        return render(request, 'tech-index.html', {'form': form})

class NewsList(View):
    def get(self, request):
        news_list = NewsModel.objects.all()
        return render(request, 'tech-index.html', {'news_list': news_list})

class NewsDetail(View):
    def get(self, request, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        return render(request, 'news_detail.html', {'news': news})

class NewsDelete(View):
    def get(self, request, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        return render(request, 'index.html', {'news': news})

    def post(self, request, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        news.delete()
        return redirect('news_list')

class сultural(View):
    def get(self, request):
        cultural_news = сultural.objects.all()
        return render(request, 'cultural.html', {'cultural':cultural_news})

class National(View):
    def get(self, request):
        national_news = National.objects.all()
        return render(request, 'national-news.html', {'national':national_news})
class Tech_science(View):
    def get(self, request):
        tech_news = Tech_science.objects.all()
        return render(request, 'tech-science.news.html', {'tech': tech_news})

class  World_news(View):
    def get(self, request):
        world_news = World_news.objects.all()
        return render(request, 'world-news.html', {'world':world_news})

