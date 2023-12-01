from injector import inject
from reports_module.modules.connected_report.interfaces.i_connected_report_repository import (
    IConnectedReportRepository,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_service import (
    IConnectedReportService,
)


class ConnectedReportService(IConnectedReportService):
    @inject
    def __init__(self, connectedReportRepo: IConnectedReportRepository):
        self.connectedReportRepo = connectedReportRepo

    def execute(self):
        pass

    def get_one(self):
        return self.connectedReportRepo.findOneById("id")
