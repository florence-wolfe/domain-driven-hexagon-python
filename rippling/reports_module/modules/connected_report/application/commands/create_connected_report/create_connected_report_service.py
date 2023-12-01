from injector import inject
from reports_module.modules.connected_report.interfaces.i_connected_report_mapper import (
    IConnectedReportMapper,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_repository import (
    IConnectedReportRepository,
)
from .interfaces.i_create_connected_report_service import (
    ICreateConnectedReportService,
)


class CreateConnectedReportService(ICreateConnectedReportService):
    @inject
    def __init__(
        self,
        connectedReportRepo: IConnectedReportRepository,
        mapper: IConnectedReportMapper,
    ):
        self.connectedReportRepo = connectedReportRepo
        self.mapper = mapper

    def execute(self, data):
        connected_report = self.mapper.to_domain(data)
        self.connectedReportRepo.insert(connected_report)
        return connected_report
