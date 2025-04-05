from django.contrib import admin
from django.urls import path

from tinyurl.views import LinkView, LinkResolutionView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/link/", LinkView.as_view(), name="link-create"),
    # Link ma być krótki, stąd krótki przedrostek "r".
    path("r/<int:pk>/", LinkResolutionView.as_view(), name="link-resolution"),
]
