from django.urls import path
from django import forms
from news import forms
# from news.views import (
#     NewsCreateView, NewsUpdateView, NewsListView, NewsDetailView, NewsDeleteView,
#     cultural_news, world_news, national_news, tech_science_page
# )
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from .views import HomePage


from django.urls import path
from news.views import (
    HomePage,
    NewsCreateView,
    NewsUpdate,
    NewsList,
    NewsDetail,
    NewsDelete,
    сultural,
    National,
    Tech_science,
    World_news,
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('update/<int:pk>/', NewsUpdate.as_view(), name='news_update'),
    path('list/', NewsList.as_view(), name='news_list'),
    path('detail/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('delete/<int:pk>/', NewsDelete.as_view(), name='news_delete'),
    path('cultural/', сultural.as_view(), name='cultural'),
    path('national/', National.as_view(), name='national'),
    path('tech-science/', Tech_science.as_view(), name='tech_science'),
    path('world-news/', World_news.as_view(), name='world_news'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
