from typing import Protocol
from reports_module.core.ddd.repository_base import BaseRepository
from reports_module.modules.embedded_report.domain.entities.embedded_report_entity import (
    EmbeddedReportEntity,
)


class IEmbeddedReportRepository(BaseRepository[EmbeddedReportEntity], Protocol):
    ...
