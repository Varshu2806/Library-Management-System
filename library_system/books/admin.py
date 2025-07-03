from django.contrib import admin
from .models import Book,Author,Member

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'total_copies','price')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    list_display=('user','bio')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=("contact_info",'user','email')




