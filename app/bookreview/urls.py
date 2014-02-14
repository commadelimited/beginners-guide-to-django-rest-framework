from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from bookreview import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^authors/$', views.AuthorView.as_view(), name='author-view'),
    url(r'^authors/(?P<pk>[\d]+)/$', views.AuthorInstanceView.as_view(), name='author-instance'),

    url(r'^books/$', views.BookView.as_view(), name='book-view'),
    url(r'^books/(?P<pk>[\d]+)/$', views.BookInstanceView.as_view(), name='book-instance'),

)

urlpatterns = format_suffix_patterns(urlpatterns)