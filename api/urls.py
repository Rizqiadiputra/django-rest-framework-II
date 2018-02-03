from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
# from . import views

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

#     #cara lima
#     #api endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^students/$', views.StudentList.as_view(), name='student-list'),
#     url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view(), name='student-detail'),
#     url(r'^students/(?P<pk>[0-9]+)/highlight/$', views.StudentHighlight.as_view(), name='student-highlight'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
# ])


# #cara ke 6
#
# #using routers
# from django.conf.urls import url,include
# from rest_framework.routers import DefaultRouter
# from . import views
#
# #create a router and register our viewsets with it
# router = DefaultRouter()
# router.register(r'students', views.StudentViewSet)
# router.register(r'users', views.UserViewSet)
#
# #the API URLs are now determined automatically by the router
# urlpatterns = [
#     url(r'^', include(router.urls))
# ]

#
# #bind ViewSet classes into a set of concrete views
#
# from .views import StudentViewSet, UserViewSet, api_root
#
# student_list = StudentViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# student_detail = StudentViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# student_highlight = StudentViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^students/$', student_list, name='student-list'),
#     url(r'^students/(?P<pk>[0-9]+)/$', student_detail, name='student-detail'),
#     url(r'^students/(?P<pk>[0-9]+)/highlight/$', student_highlight, name='student-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ])
#



#cara ke 7

#using schema view with coreapi

from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views

#create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'users', views.UserViewSet)

#the API URLs are now determined automatically by the router
schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),

]

