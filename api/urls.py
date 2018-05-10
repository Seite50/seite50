from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.author import CreateAuthorView, DetailsAuthorView
from api.views.book import CreateBookView, DetailsBookView

urlpatterns = {
    url(r'^api/book/$', CreateBookView.as_view(), name="create"),
    url(r'^api/book/(?P<pk>[0-9]+)/$',
        DetailsBookView.as_view(),
        name="details"),
    url(r'^api/author/$', CreateAuthorView.as_view(), name="create"),
    url(r'^api/author/(?P<pk>[0-9]+)/$',
        DetailsAuthorView.as_view(),
        name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)
