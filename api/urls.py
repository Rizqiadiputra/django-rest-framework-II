from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #cara satu dan dua
    # url(r'^students/$', views.student_list),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.student_detail),

    #cara tiga (class based view)
    # url(r'^students/$', views.StudentList.as_view()),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),

    # cara empat (class based view, authenticantion and autorization)
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)