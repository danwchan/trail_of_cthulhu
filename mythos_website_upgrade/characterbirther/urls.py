from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.conf import settings

from . import views

from .views import BuildWizard

urlpatterns = [  
    url(r'^$', TemplateView.as_view(template_name='characterbirther/main.html')),
#    url(r'^build$', views.browse_options, name='make_investigator'),
    url(r'^build/(?P<step>[a-z]{0,10})$', BuildWizard.as_view(url_name='build_step'), name='build_step'),
    url(r'^character/(.{7})$', views.finished_character, name='finished_character '),
    url(r'^test_result$', TemplateView.as_view(template_name='characterbirther/debug_success.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
