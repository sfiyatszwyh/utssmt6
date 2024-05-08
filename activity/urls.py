from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ActivityViewSet, ScheduleViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
