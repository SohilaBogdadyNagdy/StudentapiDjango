from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getall/', views.student_get),
    url(r'^add/',views.post_student),
    url (r'^remove/([0-9]{3})/',views.removestudent)

]
