from django.db import transaction
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from posts.models import Post, Comment, Wallet
import json


class WalletView(View):
    def post(self, request):
        name = request.POST.get('name')
        currency = request.POST.get('currency')
        balance = request.POST.get('balance')

        if not name or not currency or not balance:
            return HttpResponseBadRequest('Name, currency and balance are required')

        new_wallet = Wallet(name=name, balance=balance, currency=currency)
        new_wallet.save()

        return JsonResponse(
            {'name': new_wallet.name, 'currency': new_wallet.currency, 'balance': new_wallet.balance})

    def get(self, request):
        wallets = Wallet.objects.all()
        result = []

        render_template = render(request, 'wallet/wallet.jinja', {'wallets': wallets})
        return HttpResponse(render_template)
