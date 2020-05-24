from django.contrib import admin


from .models import Meals,Category

class MealsAdmin(admin.ModelAdmin):
	list_display = ['name','category','preperation_time','price']
	search_fields = ['name','description']
	list_filter = ['category','people']

admin.site.register(Meals,MealsAdmin)
admin.site.register(Category)
