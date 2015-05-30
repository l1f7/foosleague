from django.contrib import admin
from .models import Player


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):

    '''
        Admin View for Player
    '''
    list_display = ('nickname', 'user',)
    readonly_fields = ('created', 'modified',)
    search_fields = ['nickname', 'user', ]

admin.site.register(Player, PlayerAdmin)
