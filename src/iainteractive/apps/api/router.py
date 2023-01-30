"""Api Router"""


from rest_framework.routers import DefaultRouter

from iainteractive.apps.api.viewsets import ApplicantViewSet, GrimoriesViewSet

router = DefaultRouter()
router.register(r"grimories", GrimoriesViewSet, basename="grimorie")
router.register(r"applicants", ApplicantViewSet, basename="applicant")

urlpatterns = router.urls
