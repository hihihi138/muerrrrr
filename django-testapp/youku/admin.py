from django.contrib import admin
from youku.models import Video, User, Comment, Log

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Log)
