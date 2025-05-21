from django.http import JsonResponse
from .models import BlacklistedClient

class BlockBlacklistedClientsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        if request.method == 'POST':
            client = BlacklistedClient.objects.filter(ip_address=ip, is_active=True).first()
            if client:
                return JsonResponse({
                    'error': 'Votre accès est bloqué en raison d\'activités suspectes.',
                    'ip': ip,
                    'raison': client.reason
                }, status=403)

        return self.get_response(request)
