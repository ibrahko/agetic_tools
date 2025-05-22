from rest_framework.views import exception_handler
import sentry_sdk

def custom_exception_handler(exc, context):
    # appel du handler DRF par défaut
    response = exception_handler(exc, context)

    # on envoie à Sentry si ce n’est pas une erreur 500
    if response is not None and response.status_code != 500:
        sentry_sdk.capture_exception(exc)

    return response
