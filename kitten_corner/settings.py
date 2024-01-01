from django.conf import settings

# Get the `THE_SITE_NAME` from the main project settings file or use a default of "Kitten Corner":
THE_SITE_NAME = getattr(settings, "THE_SITE_NAME", "Kitten Corner")
