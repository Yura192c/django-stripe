from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from rest_framework.decorators import api_view
from .models import Item
import stripe
from django.conf import settings
from django.views import View
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['GET'])
def get_checkout_session_id(request, id):
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        # payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success'),
        cancel_url=request.build_absolute_uri(item.get_absolute_url()),
    )

    return JsonResponse(session, status=200)


@require_GET
def item(request, id):
    item = Item.objects.get(id=id)
    return render(request, "item.html", {"item": item,
                                         "stripe_key": settings.STRIPE_PUBLISHABLE_KEY})


class SuccessView(View):
    def get(self, request):
        return render(request, 'success.html', status=200)
