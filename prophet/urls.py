from django.conf.urls import url
from django.views import static
from django.conf import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATICFILES_DIRS[0]}, name='static'),
]

urlpatterns += [
    url(r'^stock/ping$', 'stock.views.ping'),
    url(r'^stock/index$', 'stock.views.index'),
]
