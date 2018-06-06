from django.contrib import admin
from blog.models import BlogPost,Category
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','body','category','timestamp']
admin.site.register(BlogPost,BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
admin.site.register(Category,CategoryAdmin)