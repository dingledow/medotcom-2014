from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'excerpt']
    # fields to filter the change list with
    save_on_top = True
    # fields to search in change list
    search_fields = ['title', 'excerpt', 'text']
    # enable the date drill down on change list
    date_hierarchy = 'pub_date'
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
