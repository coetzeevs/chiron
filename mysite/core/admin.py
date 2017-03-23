from django.contrib import admin

# Register your models here.
from .models import Profile, ContactUs


class ProfileAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('user', 'location','birth_date','email_confirmed')



class ContactUsAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,               {'fields': ['user']}),
	#	('Date information', {'fields': ['location']}),
	#]
	#inlines = [ChoiceInline]
	#list_filter = ['pub_date']
	#search_fields = ['question_text']
	list_display = ('surname','email','subject', 'email_body', 'phone_number', 'current_occupation', 'location')


admin.site.register(Profile,ProfileAdmin)

admin.site.register(ContactUs,ContactUsAdmin)