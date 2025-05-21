import bleach
from django.conf import settings

class BleachSanitizeMixin:
    """
    Nous avllons creer ce mixin pour la reutiliser dans tout nos serializers  pour nettoyer les champs texte avec bleach.
    Protège contre les attaques XSS (Stored/Reflected) en analysant et nettoyant tout gnamagnama.
    """
    def sanitize_input(self, key, value):
        # On exclut les champs explicitement définis dans settings
        if key in getattr(settings, "BLEACH_EXCLUDE_FIELDS", []):
            return value
        # On exclut les champs qui ne sont pas de type texte
        if isinstance(value, str):
            return bleach.clean(
                value,
                tags=getattr(settings, "BLEACH_ALLOWED_TAGS", []),
                attributes=getattr(settings, "BLEACH_ALLOWED_ATTRIBUTES", {}),
                strip=True # Supprime les balises non autorisé
            )
        # si la valeur est un dictionnaire on nettoie chaque clé valeur
        elif isinstance(value, dict):
            return {k: self.sanitize_input(k, v) for k, v in value.items()}
        # si la valeur est une liste on nettoie chaque élément de la liste
        elif isinstance(value, list):
            return [self.sanitize_input(key, item) for item in value]

        return value

    def to_internal_value(self, data):
        """
        Cette méthode est appelée avant la validation des données dans un serializer DRF.
        Elle permet d'intercepter et de nettoyer les données entrantes.
        """
        cleaned_data = {} # Dictionnaire pour stocker les données nettoyées
        # On parcourt chaque clé-valeur du dictionnaire de données
        for key, value in data.items():
            # On nettoie la valeur en fonction de la clé
            cleaned_data[key] = self.sanitize_input(key, value)
        # On appelle la méthode parente pour continuer le traitement normal de la validation normal
        return super().to_internal_value(cleaned_data)
