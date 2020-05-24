from django.contrib import admin


from .models import Post, Category,Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','auther','created','category']
	search_fields = ['title','content']
	list_filter = ['tags','category']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)

