from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
    #cara satu dan dua
    # url(r'^students/$', views.student_list),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.student_detail),

    #cara tiga (class based view)
    # url(r'^students/$', views.StudentList.as_view()),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),

    # cara empat (class based view, authenticantion and autorization)
    # url(r'^students/$', views.StudentList.as_view()),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

    #cara lima
    #api endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^students/$', views.StudentList.as_view(), name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view(), name='student-detail'),
    url(r'^students/(?P<pk>[0-9]+)/highlight/$', views.StudentHighlight.as_view(), name='student-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
])





