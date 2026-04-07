from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet

# DRF默认路由，自动生成5个API接口
router = DefaultRouter()
router.register(r'', WorkoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
