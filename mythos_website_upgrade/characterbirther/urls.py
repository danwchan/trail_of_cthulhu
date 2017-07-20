from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.conf import settings

from . import views

urlpatterns = [  
    url(r'^$', TemplateView.as_view(template_name='characterbirther/main.html')),
    url(r'^build$', views.browse_options, name='make_investigator'),
    url(r'^build/(?P<wizard>[a-z]{5,10})$', views.TEST_browse_options, name='build_forms'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
