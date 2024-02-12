"""
URL configuration for identity_protocol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from claim_identity import views as index_views  # Import views module
from . import views  # Import views for your new models

urlpatterns = [
    path('claim_identity', index_views.index, name='index'),  # Existing path

    # URLs for UserWallet
    path('userwallet/create/', views.create_user_wallet, name='create_user_wallet'),
    path('userwallet/<str:wallet_address>/', views.view_user_wallet, name='view_user_wallet'),

    # URLs for Transaction
    path('transaction/create/', views.create_transaction, name='create_transaction'),
    path('transaction/<str:transaction_id>/', views.view_transaction, name='view_transaction'),

    # URLs for Claim
    path('claim/create/', views.create_claim, name='create_claim'),
    path('claim/<str:claim_id>/', views.view_claim, name='view_claim'),

    # URLs for IdentityOwner
    path('identityowner/create/', views.create_identity_owner, name='create_identity_owner'),
    path('identityowner/<str:owner_id>/', views.view_identity_owner, name='view_identity_owner'),

    # Django admin path
    #path('admin/', admin.site.urls),
]

