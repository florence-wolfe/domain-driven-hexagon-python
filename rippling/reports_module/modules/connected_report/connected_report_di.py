from injector import Module, provider, singleton
from common.database import Database
from reports_module.modules.connected_report.application.commands.create_connected_report.create_connected_report_service import (
    CreateConnectedReportService,
)
from reports_module.modules.connected_report.infrastructure.connected_report_mapper import (
    ConnectedReportMapper,
)
from reports_module.modules.connected_report.application.connected_report_service import (
    ConnectedReportService,
)
from reports_module.modules.connected_report.infrastructure.database.connected_report_repository import (
    ConnectedReportRepository,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_mapper import (
    IConnectedReportMapper,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_repository import (
    IConnectedReportRepository,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_service import (
    IConnectedReportService,
)
from reports_module.modules.connected_report.application.commands.create_connected_report.interfaces.i_create_connected_report_service import (
    ICreateConnectedReportService,
)


class ConnectedReportModule(Module):
    @singleton
    @provider
    def provide_connected_report_repository(
        self, connectedReportMapper: IConnectedReportMapper
    ) -> IConnectedReportRepository:
        db = Database()
        return ConnectedReportRepository(db, connectedReportMapper)

    @singleton
    @provider
    def provide_connected_report_service(
        self, connectedReportRepo: IConnectedReportRepository
    ) -> IConnectedReportService:
        return ConnectedReportService(connectedReportRepo)

    @singleton
    @provider
    def provide_create_connected_report_service(
        self,
        connectedReportRepo: IConnectedReportRepository,
        connectReportMapper: IConnectedReportMapper,
    ) -> ICreateConnectedReportService:
        return CreateConnectedReportService(connectedReportRepo, connectReportMapper)

    @singleton
    @provider
    def provide_connected_report_mapper(self) -> IConnectedReportMapper:
        return ConnectedReportMapper()
