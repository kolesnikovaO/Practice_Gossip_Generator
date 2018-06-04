from django.contrib import admin
from .models import Gossip
from .models import Character

# Register your models here.
admin.site.register(Gossip)
admin.site.register(Character)