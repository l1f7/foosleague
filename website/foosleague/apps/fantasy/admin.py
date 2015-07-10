from django.contrib import admin

from .models import FanHistory, FantasySetting


class FanHistoryAdmin(admin.ModelAdmin):
    '''
        Admin View for FanHistory
    '''
    list_display = ('player', 'match', 'fans',)
    list_filter = ('player',)
    raw_id_fields = ('player', 'match',)
    readonly_fields = ('created', 'modified',)
    search_fields = ['player',]

admin.site.register(FanHistory, FanHistoryAdmin)


class FantasySettingAdmin(admin.ModelAdmin):
    '''
        Admin View for FantasySetting
    '''
    list_display = ('player',)
    list_filter = ('player',)

    raw_id_fields = ('player', )
    readonly_fields = ('created', 'modified',)
    search_fields = ['player']

admin.site.register(FantasySetting, FantasySettingAdmin)