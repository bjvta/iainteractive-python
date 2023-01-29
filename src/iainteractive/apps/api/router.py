"""Api Router"""


from iainteractive.apps.api.viewsets import ApplicantViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'applicants', ApplicantViewSet, basename='user')

urlpatterns = router.urls