from settings import STATIC_URL

def static_url(request):
    """Adds STATIC_URL to the request context"""
    return { 'STATIC_URL': STATIC_URL }