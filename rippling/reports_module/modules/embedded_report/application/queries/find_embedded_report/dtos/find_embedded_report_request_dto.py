from reports_module.core.ddd.dto_base import BaseDTO

from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


class FindEmbeddedReportRequestDTO(BaseDTO):
    id: str
    title: str
    status: ReportStatus
