from urllib.parse import urljoin

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Link(models.Model):
    """
    Model reprezentujący url przesłany przez użytkownika do skrócenia. Jako sufix skróconego urla użyte zostanie ID -
    ze względu na prostote rozwiązania. Ma ono swoje wady (użytkownik może domyśleć się, jakie są inne potencjalne
    skrócone urle i wejść na losowy). Alternatywnym rozwiązaniem jest np. użycie losowego, unikalnego ciągu znaków.
    """

    # TextField - skoro aplikacja ma służyć do skracania urli, to mogą być one potencjalnie bardzo długie - ograniczanie
    # długości przez użycie URLField wydaje się mijać z celem. Dodatkowo różne backendy bazodanowe mają różne
    # ograniczenia co do maksymalnej długości, więc maksymalny input użytkownika lepiej ograniczyć od strony API.
    original_url = models.TextField(_("original url"))

    @property
    def short_url(self):
        return urljoin(
            settings.APPLICATION_HOST, reverse("link-resolution", kwargs={"pk": self.pk})
        )

    class Meta:
        verbose_name = _("link")
        verbose_name_plural = _("links")
