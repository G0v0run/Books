from django.apps import AppConfig


class KootsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Koots'

    def ready(self):
        import Koots.Chehovs_bot
