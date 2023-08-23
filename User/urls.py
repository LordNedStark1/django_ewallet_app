from rest_framework import routers

from User import views

router = routers.DefaultRouter()
router.register('users/', views.UserViewSet)