from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('user', 'location','birth_date','email_confirmed')

admin.site.register(Profile,ProfileAdmin)