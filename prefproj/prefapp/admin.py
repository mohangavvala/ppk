from django.contrib import admin
from prefapp.models import Post

# Register your models here.
class Post_Admin(admin.ModelAdmin):
    list_display=['name','mail','mnumber','msg']
admin.site.register(Post,Post_Admin)
