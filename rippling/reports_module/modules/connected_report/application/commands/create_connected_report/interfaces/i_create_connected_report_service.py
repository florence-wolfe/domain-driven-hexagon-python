from typing import Protocol
from reports_module.core.ddd.service_base import BaseService
from reports_module.modules.connected_report.application.commands.create_connected_report.create_connected_report_command import (
    CreateConnectedReportCommand,
)
from reports_module.modules.connected_report.domain.entities.connected_report_entity import (
    ConnectedReportEntity,
)


class ICreateConnectedReportService(
    BaseService[CreateConnectedReportCommand, ConnectedReportEntity], Protocol
):
    ...
