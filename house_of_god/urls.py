from django.conf.urls import url
from django.contrib import admin

from house_of_god.assignment.api import PostList

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    url(r'^admin/', admin.site.urls),
    url(r'^get_data/', PostList.as_view(), name='post-list')

]
