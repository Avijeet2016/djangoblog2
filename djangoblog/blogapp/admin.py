from django.contrib import admin
from . models import Author, Category, Article, Comment
# Register your models here.
class AuthorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]
    class Meta:
        Model = Author

admin.site.register(Author, AuthorModel)

class ArticleModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__"]
    list_per_page = 10
    list_filter = ["posted_on", "category"]
    class Meta:
        Model = Article

admin.site.register(Article, ArticleModel)

class CategoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model = Category

admin.site.register(Category, CategoryModel)

class CommentModel(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model = Comment

admin.site.register(Comment, CommentModel)
