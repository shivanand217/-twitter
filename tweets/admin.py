from django.contrib import admin

# Bring all the models
# and Register models here.

from .forms import TweetModelForm
from .models import Twee_t


class TweetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Twee_t

admin.site.register(Twee_t, TweetModelAdmin)