from django.urls import re_path as url, include

urlpatterns = [
    url(r"^reports/", include("reports_module.core.api.urls")),
]
