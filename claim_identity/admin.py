from django.contrib import admin
from .models import UserWallet, Transaction, Claim, IdentityOwner, Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

# Admin class for UserWallet
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_address', 'metamask_installed')
    search_fields = ('user', 'wallet_address')

# Admin class for Transaction
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'token_amount', 'transaction_date')
    search_fields = ('transaction_id', 'user')

# Admin class for Claim
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('claim_id', 'user', 'successful', 'claim_date')
    search_fields = ('claim_id', 'user')

# Admin class for IdentityOwner
class IdentityOwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'is_claimed')
    search_fields = ('owner_id',)

# Registering models with the admin
admin.site.register(UserWallet, UserWalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(IdentityOwner, IdentityOwnerAdmin)
