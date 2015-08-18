from django.contrib import admin

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fields = ['url', 'text', 'headline', 'description']

admin.site.register(Post)