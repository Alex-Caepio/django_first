import json

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views import View

from posts.models import Wallet


class EditWalletView(View):

    def post(self, request, wallet_id):
        wallet = Wallet.objects.get(id=wallet_id)
        name = request.POST.get('name')
        currency = request.POST.get('currency')
        balance = request.POST.get('balance')

        if not name or not currency or not balance:
            return HttpResponseBadRequest('Name, currency and balance are required')

        wallet.name = name
        wallet.currency = currency
        wallet.balance = balance
        wallet.save()

        return JsonResponse(
            {'name': wallet.name, 'currency': wallet.currency, 'balance': wallet.balance})
