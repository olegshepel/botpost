from rest_framework.routers import DefaultRouter

from posts.api.views import *

router = DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns = router.urls
