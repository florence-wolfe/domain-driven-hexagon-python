from typing import Protocol
from reports_module.core.ddd.service_base import BaseService
from reports_module.modules.embedded_report.domain.entities.embedded_report_entity import (
    EmbeddedReportEntity,
)


class IEmbeddedReportService(BaseService, Protocol):
    def get_connected_report_with_custom_status(self) -> EmbeddedReportEntity:
        ...
