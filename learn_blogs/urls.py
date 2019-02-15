from django.urls import path,re_path
from . import views

app_name="learn_blogs"
urlpatterns=[
    re_path(r'^$',views.index,name='index'),
    re_path(r'topics/$',views.topics,name='topics'),
    re_path(r'topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
]
