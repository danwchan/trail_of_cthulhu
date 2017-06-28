from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings

from .views import CharacterOptionsView, Occupations

urlpatterns = [  
    url(r'^.*1$', CharacterOptionsView.as_view(), name='make_investigator'),
    url(r'^.*2$', Occupations.as_view(), name='make_investigator'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
