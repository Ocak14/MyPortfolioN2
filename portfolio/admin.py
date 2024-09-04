from django.contrib import admin
from django.shortcuts import render
from .models import Contact,About,Portfolio,We_do
from django.utils.html import format_html

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","phone_number","email")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  
  
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  

@admin.register(We_do)
class We_doAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  