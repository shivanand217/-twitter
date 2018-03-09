from django.contrib import admin

# Bring all the models
# and Register your models.

from .models import Tweet

admin.site.register(Tweet)