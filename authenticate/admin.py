from django.contrib import admin

# Register your models here.
from .models import WatchList, StreamingService

admin.site.register(WatchList)
admin.site.register(StreamingService)

