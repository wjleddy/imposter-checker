from django.contrib import admin
from .models import BaseHandle, SimilarHandles

admin.site.register(BaseHandle)
admin.site.register(SimilarHandles)
