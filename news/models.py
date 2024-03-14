from django.db import models


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'News category'
        verbose_name_plural = 'News categories'


class NewsModel(models.Model):
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
        verbose_name = 'Announcement'
        verbose_name_plural = 'News'
