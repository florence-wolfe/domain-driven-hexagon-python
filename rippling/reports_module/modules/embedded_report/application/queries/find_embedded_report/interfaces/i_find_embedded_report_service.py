from typing import Protocol
from reports_module.core.ddd.service_base import BaseService


class IFindEmbeddedReportService(BaseService, Protocol):
    ...
