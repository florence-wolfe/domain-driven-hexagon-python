from injector import inject
from reports_module.modules.connected_report.interfaces.i_connected_report_service import (
    IConnectedReportService,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_mapper import (
    IEmbeddedReportMapper,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_service import (
    IEmbeddedReportService,
)


class EmbeddedReportService(IEmbeddedReportService):
    @inject
    def __init__(
        self,
        connectedReportService: IConnectedReportService,
        mapper: IEmbeddedReportMapper,
    ):
        self.mapper = mapper
        self.connectedReportService = connectedReportService

    def execute(self):
        pass

    def get_connected_report_with_custom_status(self):
        custom_report = self.connectedReportService.get_one()
        return custom_report
