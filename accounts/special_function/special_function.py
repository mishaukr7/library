from django.utils.http import is_safe_url, urlunquote


def get_next_url(request):
    next = request.META.get('HTTP_REFERER')
    if next:
        next = urlunquote(next)
    if not is_safe_url(next, host=request.get_host()):
        next = '/'
    return next
