# from rest_framework.throttling import SimpleRateThrottle

# class IPBlacklistThrottle(SimpleRateThrottle):
#     scope = 'ip_blacklist'

#     def get_cache_key(self, request, view):
#         ip = self.get_ident(request)

#         try:
#             blocked = BlacklistedClient.objects.get(ip_address=ip)
#             if blocked.is_active:
#                 return self.cache_format % {
#                     'scope': self.scope,
#                     'ident': f'blocked-{ip}'
#                 }
#         except BlacklistedClient.DoesNotExist:
#             pass

#         return super().get_cache_key(request, view)
