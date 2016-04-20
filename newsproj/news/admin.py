from django.contrib import admin

# Register your models here.importing from models
from .models import Feed, Article

admin.site.register(Feed)
admin.site.register(Article)