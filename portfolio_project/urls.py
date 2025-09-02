from django.contrib import admin
from django.urls import path, include

# serving media files for development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("my-work/", include("mywork.urls")),
    path("page", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

# serving media files for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
