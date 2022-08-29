from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from OrgLink.api.views import OrgLinkViewSet

router = routers.DefaultRouter()
router.register("orglink", OrgLinkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
