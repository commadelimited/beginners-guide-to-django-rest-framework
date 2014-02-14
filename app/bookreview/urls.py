from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from bookreview.views import index_view, AuthorView

urlpatterns = patterns(
    '',
    url(r'^$', index_view, name='index_view'),
    url(r'^authors/$', AuthorView.as_view(), name='author-view'),

)

urlpatterns = format_suffix_patterns(urlpatterns)