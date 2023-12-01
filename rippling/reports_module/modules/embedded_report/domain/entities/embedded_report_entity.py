from typing import Protocol
from reports_module.core.ddd.entity_base import Entity


class EmbeddedReportEntity(Entity, Protocol):
    pass
