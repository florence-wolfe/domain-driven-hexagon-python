from reports_module.modules.connected_report.infrastructure.database.connected_report_model import (
    ConnectedReportModel,
)
from reports_module.modules.connected_report.domain.entities.connected_report_entity import (
    ConnectedReportEntity,
    ConnectedReportProps,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_mapper import (
    IConnectedReportMapper,
)


class ConnectedReportMapper(IConnectedReportMapper):
    def to_domain(self, record):
        # Mapping logic from Database object to Domain object
        props = ConnectedReportProps(title=record.title, status=record.status)
        return ConnectedReportEntity.create(props)

    def to_persistence(self, entity):
        # Mapping logic from Domain object to Database object
        return ConnectedReportModel(
            title=entity.props["title"],
            status=entity.props["status"],
        )

    def to_response(self, entity):
        return entity
