from pydantic import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from injector import inject
from reports_module.core.api.viewset_base import BaseViewSet
from reports_module.modules.embedded_report.application.queries.find_embedded_report.dtos.find_embedded_report_request_dto import (
    FindEmbeddedReportRequestDTO,
)
from reports_module.modules.embedded_report.application.queries.find_embedded_report.dtos.find_embedded_report_response_dto import (
    FindEmbeddedReportResponseDTO,
)
from reports_module.modules.embedded_report.application.queries.find_embedded_report.find_embedded_report_query import (
    FindEmbeddedReportQuery,
)
from reports_module.modules.embedded_report.application.queries.find_embedded_report.interfaces.i_find_embedded_report_service import (
    IFindEmbeddedReportService,
)


class FindEmbeddedReportController(BaseViewSet):
    @inject
    def __init__(
        self, find_embedded_report_service: IFindEmbeddedReportService, **kwargs
    ):
        super().__init__(**kwargs)
        self.find_embedded_report_service = find_embedded_report_service

    def list(self, request: Request):
        try:
            d = request.query_params.dict()
            dto = FindEmbeddedReportRequestDTO(**d)
        except ValidationError as e:
            return Response(e.errors(), status=400)

        command = FindEmbeddedReportQuery(**dto.model_dump())
        result = self.find_embedded_report_service.execute(command)
        response_dto = FindEmbeddedReportResponseDTO(
            id=str(result["_id"]), **result["props"]
        )

        return Response(status=200, data=response_dto.model_dump())
