from django.http import HttpResponse
from django.views import View

from posts.models import Wallet


class DeleteWallet(View):
    def get(self, request, wallet_id):
        wallet = Wallet.objects.get(id=wallet_id)
        wallet.delete()
        return HttpResponse('Wallet deleted')
