from django.contrib import admin
from . models import Page, Like
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'page_cat', 'page_publish_date', 'user') 
    
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('paata', 'page_name', 'page_cat', 'page_publish_date', 'user', 'likes' ) 