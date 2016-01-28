from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
)
