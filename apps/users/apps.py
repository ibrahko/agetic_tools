from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    #il faut l'annonce pour que le signale soient declenché
    def ready(self):
        import apps.users.signals
