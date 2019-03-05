from django.conf.urls import url
from courses.views import (ListCreateCourse, RetrieveUpdateDestroyCourse,
                            ListCreateReview, RetrieveUpdateDestroyReview
                            )

app_name = 'courses'
urlpatterns = [
    url(r'^$', ListCreateCourse.as_view(), name='course_list'),
    url(r'(?P<pk>\d+)/$', RetrieveUpdateDestroyCourse.as_view(), name='detail'),
    url(r'^(?P<course_pk>\d+)/reviews/$', ListCreateReview.as_view(), name='review_list'),
    url(r'^(?P<course_pk>\d+)/reviews/$/(?P<pk>\d+)/$', RetrieveUpdateDestroyReview.as_view,
                                                name='review_details'),
]