
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Wing.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('account/', include('account.urls')),
    path('api/', include('api.urls')),
]
