from django.contrib import admin
from .models import BookData, BookChapterData
# Register your models here.

admin.site.register(BookData)
admin.site.register(BookChapterData)