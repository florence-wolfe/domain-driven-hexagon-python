from pydantic import BaseModel

from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


class FindEmbeddedReportQuery(BaseModel):
    title: str
    status: ReportStatus
