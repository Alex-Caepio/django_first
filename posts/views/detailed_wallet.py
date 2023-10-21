from django.db import transaction
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from posts.models import Post, Comment, Wallet
import json


class DetailedWallet(View):
    def get(self, request, wallet_id):
        wallet = Wallet.objects.get(id=wallet_id)
        render_template = render(request, 'wallet/wallet_details.jinja', {'wallet': wallet})
        return HttpResponse(render_template)
