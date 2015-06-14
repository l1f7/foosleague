from django.contrib import admin
from .models import Player, StatHistory, ExposeHistory
ExposeHistory

class StatHistoryInline(admin.TabularInline):
        '''
            Tabular Inline View for StatHistory
        '''
        model = StatHistory
        extra = 0
        raw_id_fields = ('match',)

class ExposeHistoryInline(admin.TabularInline):
        '''
            Tabular Inline View for ExposeHistory
        '''
      model = ExposeHistory
      extra = 0
      raw_id_fields = ('match',)

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):

    '''
        Admin View for Player
    '''
    list_display = ('nickname', 'user', 'ts_mu', 'ts_sigma')
    readonly_fields = ('created', 'modified',)
    search_fields = ['nickname', 'user', ]
    inlines = [StatHistoryInline, ExposeHistoryInline]

admin.site.register(Player, PlayerAdmin)
