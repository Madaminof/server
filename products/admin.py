from django.contrib import admin
from .models import Book,BookCategory,Author,Review
# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
