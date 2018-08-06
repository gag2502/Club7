from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from workout import views

router = routers.DefaultRouter()
router.register(r'workout', views.WorkoutViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
 #  url(r'^api-auth/', include('rest-framework.urls', namespace='rest_framework'))
   ]
