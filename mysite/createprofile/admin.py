from django.contrib import admin

# Register your models here.
from .models import Employee_Profile,Employer_Profile, Document, Profile_Picture


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

class DocumentAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('user', 'description','document','uploaded_at')

class Profile_PictureAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('user', 'description','photo','uploaded_at')


admin.site.register(Employee_Profile,Employee_ProfileAdmin)
admin.site.register(Employer_Profile,Employer_ProfileAdmin)
admin.site.register(Document,DocumentAdmin)
admin.site.register(Profile_Picture,Profile_PictureAdmin)


