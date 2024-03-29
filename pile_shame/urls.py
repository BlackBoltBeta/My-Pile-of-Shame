from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("hobbycentre.urls"), name="hobbycentre-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]

# namespace='hobbycentre'
