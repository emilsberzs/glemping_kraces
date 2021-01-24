from django.contrib import admin

from .models import Post, Activity, Picture, Review

admin.site.register(Post)
admin.site.register(Activity)
admin.site.register(Picture)
admin.site.register(Review)
