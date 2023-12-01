from injector import Module, provider, singleton
from reports_module.modules.connected_report.interfaces.i_connected_report_service import (
    IConnectedReportService,
)
from reports_module.modules.embedded_report.infrastructure.embedded_report_mapper import (
    EmbeddedReportMapper,
)
from reports_module.modules.embedded_report.infrastructure.database.embedded_report_repository import (
    EmbeddedReportRepository,
)
from reports_module.modules.embedded_report.application.embedded_report_service import (
    EmbeddedReportService,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_mapper import (
    IEmbeddedReportMapper,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_repository import (
    IEmbeddedReportRepository,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_service import (
    IEmbeddedReportService,
)
from reports_module.modules.embedded_report.application.queries.find_embedded_report.interfaces.i_find_embedded_report_service import (
    IFindEmbeddedReportService,
)
from reports_module.modules.embedded_report.application.queries.find_embedded_report.find_embedded_report_service import (
    FindEmbeddedReportService,
)


class EmbeddedReportModule(Module):
    @singleton
    @provider
    def provide_embedded_report_repository(self) -> IEmbeddedReportRepository:
        return EmbeddedReportRepository()

    @singleton
    @provider
    def provide_embedded_report_mapper(self) -> IEmbeddedReportMapper:
        return EmbeddedReportMapper()

    @singleton
    @provider
    def provide_embedded_report_service(
        self,
        connectedReportService: IConnectedReportService,
        embeddedReportMapper: IEmbeddedReportMapper,
    ) -> IEmbeddedReportService:
        return EmbeddedReportService(connectedReportService, embeddedReportMapper)

    @singleton
    @provider
    def provide_find_embedded_report_service(
        self,
        embeddedReportMapper: IEmbeddedReportMapper,
        embeddedReportService: IEmbeddedReportService,
    ) -> IFindEmbeddedReportService:
        return FindEmbeddedReportService(embeddedReportMapper, embeddedReportService)
