from django.views.generic import RedirectView
from rest_framework.generics import CreateAPIView, get_object_or_404

from tinyurl.models import Link
from tinyurl.serializers import LinkSerializer


class LinkView(CreateAPIView):
    """
    Widok służący do generowania krótkich linków dla podanych urli.
    """
    serializer_class = LinkSerializer


class LinkResolutionView(RedirectView):
    """
    Widok służący do przekierowania użytkownika z krótkiego urla na kryjący się pod nim, oryginalny url.
    """

    def get_redirect_url(self, *args, **kwargs):
        link_obj = get_object_or_404(Link, pk=kwargs["pk"])
        return link_obj.original_url