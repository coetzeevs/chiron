from django.contrib import admin

# Register your models here.
from .models import Employee_Profile,Employer_Profile


class Employee_ProfileAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('user', 'current_company')

class Employer_ProfileAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('user', 'company')


admin.site.register(Employee_Profile,Employee_ProfileAdmin)
admin.site.register(Employer_Profile,Employer_ProfileAdmin)
