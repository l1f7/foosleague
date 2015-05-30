from django.contrib import admin
from .models import Bet, Transaction

# Register your models here.
class BetAdmin(admin.ModelAdmin):
    '''
        Admin View for Bet
    '''
    list_display = ('player', 'amount', 'match',)
    list_filter = ('match','player',)

    # raw_id_fields = ('',)
    readonly_fields = ('created', 'modified',)
    search_fields = ['player', 'match',]

admin.site.register(Bet, BetAdmin)


class TransactionAdmin(admin.ModelAdmin):
    '''
        Admin View for Transaction
    '''
    list_display = ('amount', 'match', 'bet', 'player',)
    list_filter = ('player', 'match',)

    readonly_fields = ('created', 'modified')
    search_fields = ['amount', 'match']

admin.site.register(Transaction, TransactionAdmin)