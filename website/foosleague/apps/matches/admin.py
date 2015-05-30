from django.contrib import admin
from .models import Match

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    '''
        Admin View for Match
    '''
    list_display = ('team_1', 'team_2',)
    list_filter = ('team_1', 'team_2',)

    readonly_fields = ('created', 'modified',)
    search_fields = ['team_1', 'team_2',]

admin.site.register(Match, MatchAdmin)