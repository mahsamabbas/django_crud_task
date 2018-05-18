from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from pets.api.views import PetViewSet

from project.admin import owners, admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', admin.urls),
    url(r'^owners/', owners.urls),
    url(r'^', include('pets.urls')),
]

# API ROUTES
router = routers.DefaultRouter()
router.register(r'pets', PetViewSet, base_name='pet')
urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


