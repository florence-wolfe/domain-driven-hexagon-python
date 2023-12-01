from injector import inject
from common.database import Database
from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)
from reports_module.modules.connected_report.domain.entities.connected_report_entity import (
    ConnectedReportEntity,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_mapper import (
    IConnectedReportMapper,
)
from reports_module.modules.connected_report.interfaces.i_connected_report_repository import (
    IConnectedReportRepository,
)


class ConnectedReportRepository(IConnectedReportRepository):
    @inject
    def __init__(self, db: Database, mapper: IConnectedReportMapper):
        self.db = db
        self.mapper = mapper

    def insert(self, record):
        data = self.mapper.to_persistence(record)
        return self.db.insert(data)

    def findOneById(self, _id: str):
        return ConnectedReportEntity.create(
            create_props={
                "title": "hey from PRIVATE connected report repository!",
                "status": ReportStatus.DRAFT,
            }
        )

    def findAll(self):
        return []

    def findAllPaginated(self):
        return []

    def delete(self, record):
        return

    def transaction(self):
        return
