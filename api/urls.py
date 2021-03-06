from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.author import CreateAuthorView, DetailsAuthorView
from api.views.book import CreateBookView, DetailsBookView

urlpatterns = {
    url(r'book/$', CreateBookView.as_view(), name="create_book"),
    url(r'book/(?P<pk>[0-9]+)/$',
        DetailsBookView.as_view(),
        name="details_book"),
    url(r'author/$', CreateAuthorView.as_view(), name="create_author"),
    url(r'author/(?P<pk>[0-9]+)/$',
        DetailsAuthorView.as_view(),
        name="details_author")
}

urlpatterns = format_suffix_patterns(urlpatterns)
