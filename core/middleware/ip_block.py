# from django.http import JsonResponse
# from core.models.blacklistModel import BlacklistedClient

# class IPBlockMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         ip = request.META.get('REMOTE_ADDR')
#         blocked = BlacklistedClient.objects.filter(ip_address=ip, is_active=True).first()
#         if blocked:
#             return JsonResponse({'detail': 'Votre accès est bloqué.'}, status=403)

#         return self.get_response(request)
