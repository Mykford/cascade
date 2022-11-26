from django.contrib import admin
from .models import Posts, Categories

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display =('title','author','category')
    list_filter = ('title','author','publish','status','category')
    
    date_hierarchy = ('publish')
    search_fields = ('title','author','status','category')

admin.site.register(Posts,PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter=('name',)

admin.site.register(Categories,CategoryAdmin)

