import requests
from .models import BlacklistedClient

def get_ip_geolocation(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        if response.status_code == 200:
            data = response.json()
            return {
                'location_country': data.get('country_name'),
                'location_city': data.get('city'),
                'latitude': data.get('latitude'),
                'longitude': data.get('longitude'),
            }
    except:
        pass
    return {}

def block_client(request, reason="Activité suspecte"):
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    geo_data = get_ip_geolocation(ip)

    obj, created = BlacklistedClient.objects.get_or_create(
        ip_address=ip,
        defaults={
            'mac_address': None,
            'reason': reason,
            'user_agent': user_agent,
            **geo_data
        }
    )
    if not created:
        obj.attempts += 1
        obj.reason = reason
        obj.user_agent = user_agent
        obj.is_active = True
        for k, v in geo_data.items():
            setattr(obj, k, v)
        obj.save()
