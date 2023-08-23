from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('transactions/', views.TransactionViewSet)

urlpatterns = router.urls