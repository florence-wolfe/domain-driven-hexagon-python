from pydantic_core import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from injector import inject
from reports_module.core.api.viewset_base import BaseViewSet
from reports_module.modules.connected_report.application.commands.create_connected_report.create_connected_report_command import (
    CreateConnectedReportCommand,
)
from .dtos import (
    CreateConnectedReportRequestDTO,
    CreateConnectedReportResponseDTO,
)

from .interfaces.i_create_connected_report_service import (
    ICreateConnectedReportService,
)


class CreateConnectedReportController(BaseViewSet):
    @inject
    def __init__(
        self, create_connected_report_service: ICreateConnectedReportService, **kwargs
    ):
        super().__init__(**kwargs)
        self.create_connected_report_service = create_connected_report_service

    def create(self, request: Request):
        # Some kind of validation
        if not request or not request.data:
            return Response(status=400, data="No data provided")

        try:
            dto = CreateConnectedReportRequestDTO(**request.data)
        except ValidationError as e:
            return Response(e.errors(), status=400)

        command = CreateConnectedReportCommand(**dto.model_dump())
        result = self.create_connected_report_service.execute(command)
        response_dto = CreateConnectedReportResponseDTO(
            id=str(result.id), **result.props
        )
        return Response(
            status=201,
            data=response_dto.model_dump(),
        )
