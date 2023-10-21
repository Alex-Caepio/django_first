from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from posts.models import Wallet


class EditFormRender(View):
    def get(self, request, wallet_id):
        wallet = Wallet.objects.get(id=wallet_id)
        form_created = render(request, 'wallet/wallet_update_form.jinja', {'wallet_id': wallet.id})
        return HttpResponse(form_created)
