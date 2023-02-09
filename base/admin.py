from django.contrib import admin
from .models import Post, Projects, Comment, Contact
# Register your models here.
admin.site.register(Post)
admin.site.register(Projects)
admin.site.register(Comment)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject','created', 'message')
    
admin.site.register(Contact, ContactAdmin)    