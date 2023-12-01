from typing import Protocol
from reports_module.core.ddd.repository_base import BaseRepository
from reports_module.modules.connected_report.domain.entities.connected_report_entity import (
    ConnectedReportEntity,
)


class IConnectedReportRepository(BaseRepository[ConnectedReportEntity], Protocol):
    ...
