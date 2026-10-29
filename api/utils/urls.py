from rest_framework.routers import SimpleRouter
from utils import views

router = SimpleRouter(trailing_slash=False)

router.register(r"theme", views.ThemeViewSet, basename="theme")

urlpatterns = [
    *router.urls
]