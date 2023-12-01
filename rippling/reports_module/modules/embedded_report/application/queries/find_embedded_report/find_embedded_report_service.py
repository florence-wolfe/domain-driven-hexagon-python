from injector import inject
from reports_module.modules.embedded_report.application.queries.find_embedded_report.interfaces.i_find_embedded_report_service import (
    IFindEmbeddedReportService,
)
from reports_module.modules.embedded_report.interfaces.embedded_report_dto import (
    EmbeddedReportDTO,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_mapper import (
    IEmbeddedReportMapper,
)
from reports_module.modules.embedded_report.interfaces.i_embedded_report_service import (
    IEmbeddedReportService,
)


class FindEmbeddedReportService(IFindEmbeddedReportService):
    @inject
    def __init__(
        self,
        embeddedReportMapper: IEmbeddedReportMapper,
        embeddedReportSerive: IEmbeddedReportService,
    ):
        self.mapper = embeddedReportMapper
        self.service = embeddedReportSerive

    def execute(self, dto: EmbeddedReportDTO):
        embedded_report = self.mapper.to_domain(dto)
        custom_report = self.service.get_connected_report_with_custom_status()
        custom_report_dict = custom_report.to_dict()
        return {
            **custom_report_dict,
            "extras": "BANANANA",
            "service name": "FindEmbeddedReportService",
        }
