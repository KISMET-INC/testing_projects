from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_one import views
from django.conf.urls import url

# urlpatterns = [
#     path('', include('app_one.urls')),
# ]
urlpatterns = [
    url(
        r'^$',
        views.FiraCreateView.as_view(),
        name='create',
    ),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
