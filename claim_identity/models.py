from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Models for MetaMask Integration
class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=255, unique=True)
    metamask_installed = models.BooleanField()

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(UserWallet, on_delete=models.CASCADE)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()

class Claim(models.Model):
    claim_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(UserWallet, on_delete=models.CASCADE)
    successful = models.BooleanField()
    claim_date = models.DateTimeField()

class IdentityOwner(models.Model):
    owner_id = models.CharField(max_length=255, primary_key=True)
    is_claimed = models.BooleanField()
