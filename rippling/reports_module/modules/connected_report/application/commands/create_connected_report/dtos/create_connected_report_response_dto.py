from pydantic.main import BaseModel

from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


class CreateConnectedReportResponseDTO(BaseModel):
    id: str
    title: str
    status: ReportStatus
    # Add other fields as necessary
