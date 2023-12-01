from pydantic import BaseModel

from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


class CreateConnectedReportCommand(BaseModel):
    title: str
    status: ReportStatus
