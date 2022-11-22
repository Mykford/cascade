from django.contrib import admin
from .models import Posts

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display =('title','slug','author')
    list_filter = ('title','author','publish','status')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = ('publish')
    search_fields = ('title','author','status')

admin.site.register(Posts)    

