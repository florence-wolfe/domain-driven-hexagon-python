from dataclasses import dataclass
from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


@dataclass
class ConnectedReportDTO:
    def __init__(self, title: str, status: ReportStatus):
        self.title = title
        self.status = status
