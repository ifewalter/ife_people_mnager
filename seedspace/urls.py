from django.conf.urls import url
from seedspaceapp import views

urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^add/', views.add_person),
    url(r'^list/', views.list)
]
