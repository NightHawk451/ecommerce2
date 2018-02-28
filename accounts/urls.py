from django.conf.urls import url

from .views import (
        AccountHomeView,
        UserDetailUpdateView,
        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
]