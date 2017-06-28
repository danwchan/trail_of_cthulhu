from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.conf import settings

from . import views

urlpatterns = [  
    url(r'^$', TemplateView.as_view(template_name='main.html')),
    url(r'build$', views.occupation_list, name='make_investigator'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
