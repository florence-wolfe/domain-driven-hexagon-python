from django.urls import re_path as url, include
from common.router import Router
from reports_module.modules.connected_report.application.commands.create_connected_report.create_connected_report_http_controller import (
    CreateConnectedReportController,
)
from reports_module.modules.embedded_report.application.queries.find_embedded_report.find_embedded_report_controller import (
    FindEmbeddedReportController,
)

router = Router()
router.register(
    r"connected_report", CreateConnectedReportController, basename="connected_report"
)

router.register(
    r"embedded_report", FindEmbeddedReportController, basename="embedded_report"
)

urlpatterns = [
    url("", include(router.urls)),
]
