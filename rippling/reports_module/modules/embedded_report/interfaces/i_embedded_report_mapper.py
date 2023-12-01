from typing import Any, Protocol
from reports_module.core.ddd.mapper import IMapper
from reports_module.modules.embedded_report.interfaces.embedded_report_dto import (
    EmbeddedReportDTO,
)
from reports_module.modules.embedded_report.domain.entities.embedded_report_entity import (
    EmbeddedReportEntity,
)


class IEmbeddedReportMapper(
    IMapper[EmbeddedReportEntity, EmbeddedReportDTO, Any], Protocol
):
    ...
