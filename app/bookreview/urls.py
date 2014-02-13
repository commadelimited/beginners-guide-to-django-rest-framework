from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from bookreview import views

urlpatterns = patterns(
    '',

    # Ping endpoint, which clients can hit periodically to trigger any processing tasks
    url(r'^authors/$', views.AuthorView.as_view(), name='author-view'),

)

urlpatterns = format_suffix_patterns(urlpatterns)