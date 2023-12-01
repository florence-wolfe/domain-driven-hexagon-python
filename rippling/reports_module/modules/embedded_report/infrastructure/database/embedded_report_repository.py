from reports_module.modules.embedded_report.interfaces.i_embedded_report_repository import (
    IEmbeddedReportRepository,
)


class EmbeddedReportRepository(IEmbeddedReportRepository):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def findAll(self):
        pass

    def findOneById(self, *_args):
        pass

    def findAllPaginated(self):
        pass

    def transaction(self):
        pass
