from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.make_investigator, name='make_investigator'),
]
