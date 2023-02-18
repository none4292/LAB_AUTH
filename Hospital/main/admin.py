from django.contrib import admin
from .models import Appointment, Contact, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
        list_display = ('name', 'comment')






class ContactAdmin(admin.ModelAdmin):
        list_display = ('name', 'subject', 'content')



admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)



