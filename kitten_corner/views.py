from django.http import HttpResponse

from kitten_corner.settings import THE_SITE_NAME


THE_APP_NAME = "Kitten Corner"


def index(request):
    """
    Simple function-based view to display the kitten list
    """
    return HttpResponse(
        f"<title>{THE_SITE_NAME} - {THE_APP_NAME}</title>"
        f"Hello, Kittens! You're at the {THE_SITE_NAME} : {THE_APP_NAME} site."
    )
