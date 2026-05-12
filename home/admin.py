from django.contrib import admin

from home.models import Setting, ContactMessage, Language


# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','code')

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ['status']


admin.site.register(Setting,SettingsAdmin)
admin.site.register(ContactMessage,ContactAdmin)
admin.site.register(Language,LanguageAdmin)