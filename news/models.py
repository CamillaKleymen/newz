from django.db import models
from datetime import date


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'


class NewsModel(models.Model):  # Добавлено определение модели NewsModel
    news_title = models.CharField(max_length=50)
    news_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    news_country = models.CharField(max_length=30)
    news_date = models.DateField()
    news_description = models.TextField()
    news_image = models.FileField(upload_to='news_images')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Cultural(models.Model):
    news_title = models.CharField(max_length=50)
    news_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    news_country = models.CharField(max_length=30)
    news_date = models.DateField()
    news_description = models.TextField()
    news_image = models.FileField(upload_to='news_images')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Cultural'
        verbose_name_plural = 'Cultural News'


class National_url(models.Model):
    news_title = models.CharField(max_length=50)
    news_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    news_date = models.DateField()
    news_description = models.TextField()
    news_image = models.FileField(upload_to='news_images')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'National'
        verbose_name_plural = 'National News'


class TechScience(models.Model):
    news_title = models.CharField(max_length=50)
    news_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    news_country = models.CharField(max_length=30)
    news_date = models.DateField()
    news_description = models.TextField()
    news_image = models.FileField(upload_to='news_images')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Tech & Science'
        verbose_name_plural = 'Tech & Science News'


class WorldNews(models.Model):
    news_title = models.CharField(max_length=50)
    news_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    news_country = models.CharField(max_length=30)
    news_date = models.DateField()
    news_description = models.TextField()
    news_image = models.FileField(upload_to='news_images')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'World News'
        verbose_name_plural = 'World News'
