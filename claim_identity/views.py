from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import UserWallet, Transaction, Claim, IdentityOwner
import json

def index(request):
    return HttpResponse("Hello, Degen!")

@csrf_exempt
@require_http_methods(["POST"])
def create_user_wallet(request):
    try:
        data = json.loads(request.body)
        user_wallet = UserWallet.objects.create(
            user_id=data['user_id'],  # Assuming 'user_id' is passed in the request
            wallet_address=data['wallet_address'],
            metamask_installed=data.get('metamask_installed', False)
        )
        return JsonResponse({"wallet_address": user_wallet.wallet_address}, status=201)
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@require_http_methods(["GET"])
def view_user_wallet(request, wallet_address):
    try:
        user_wallet = UserWallet.objects.get(wallet_address=wallet_address)
        return JsonResponse({
            "user_id": user_wallet.user_id,
            "wallet_address": user_wallet.wallet_address,
            "metamask_installed": user_wallet.metamask_installed
        })
    except UserWallet.DoesNotExist:
        return JsonResponse({"error": "UserWallet not found"}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def create_transaction(request):
    try:
        data = json.loads(request.body)
        transaction = Transaction.objects.create(
            transaction_id=data['transaction_id'],
            user_id=data['user_wallet_id'],
            token_amount=data['token_amount'],
            transaction_date=data['transaction_date']
        )
        return JsonResponse({"transaction_id": transaction.transaction_id}, status=201)
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@require_http_methods(["GET"])
def view_transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        return JsonResponse({
            "transaction_id": transaction.transaction_id,
            "user_wallet_id": transaction.user_id,
            "token_amount": str(transaction.token_amount),
            "transaction_date": transaction.transaction_date
        })
    except Transaction.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def create_claim(request):
    try:
        data = json.loads(request.body)
        claim = Claim.objects.create(
            claim_id=data['claim_id'],
            user_id=data['user_wallet_id'],
            successful=data['successful'],
            claim_date=data['claim_date']
        )
        return JsonResponse({"claim_id": claim.claim_id}, status=201)
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@require_http_methods(["GET"])
def view_claim(request, claim_id):
    try:
        claim = Claim.objects.get(claim_id=claim_id)
        return JsonResponse({
            "claim_id": claim.claim_id,
            "user_wallet_id": claim.user_id,
            "successful": claim.successful,
            "claim_date": claim.claim_date
        })
    except Claim.DoesNotExist:
        return JsonResponse({"error": "Claim not found"}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def create_identity_owner(request):
    try:
        data = json.loads(request.body)
        identity_owner = IdentityOwner.objects.create(
            owner_id=data['owner_id'],
            is_claimed=data['is_claimed']
        )
        return JsonResponse({"owner_id": identity_owner.owner_id}, status=201)
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@require_http_methods(["GET"])
def view_identity_owner(request, owner_id):
    try:
        identity_owner = IdentityOwner.objects.get(owner_id=owner_id)
        return JsonResponse({
            "owner_id": identity_owner.owner_id,
            "is_claimed": identity_owner.is_claimed
        })
    except IdentityOwner.DoesNotExist:
        return JsonResponse({"error": "IdentityOwner not found"}, status=404)



