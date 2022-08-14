from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(News)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Category)