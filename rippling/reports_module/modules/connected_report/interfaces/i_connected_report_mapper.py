from typing import Any, Protocol
from reports_module.core.ddd.mapper import IMapper
from reports_module.modules.connected_report.interfaces.connected_report_dto import (
    ConnectedReportDTO,
)
from reports_module.modules.connected_report.domain.entities.connected_report_entity import (
    ConnectedReportEntity,
)


class IConnectedReportMapper(
    IMapper[ConnectedReportEntity, ConnectedReportDTO, Any], Protocol
):
    ...
