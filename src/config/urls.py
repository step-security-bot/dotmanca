from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from django.views import defaults as default_views

from main.views import HomePageView

urlpatterns = [
    re_path(r"^$", HomePageView.as_view(), name="home"),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),
    # User management
    re_path(r"^users/", include("dotmanca.users.urls", namespace="users")),
    # Your stuff: custom urls includes go here
    re_path(r"^news/", include("news.urls")),
    re_path(r"^about/", include("main.urls")),
    re_path(r"^galleries/", include("gallery.urls")),
    re_path(r"^comics/", include("comics.urls")),
    re_path(r"^characters/", include("characters.urls")),
    re_path(r"^places/", include("places.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        re_path(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        re_path(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        re_path(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            re_path(r"^__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
