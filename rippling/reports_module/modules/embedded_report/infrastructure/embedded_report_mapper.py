from reports_module.modules.embedded_report.interfaces.i_embedded_report_mapper import (
    IEmbeddedReportMapper,
)


class EmbeddedReportMapper(IEmbeddedReportMapper):
    def to_domain(self, *_args):
        """return EmbeddedReportEntity(
            id=record.id,
            title=record.title,
            status=record.status,
            created_at=record.created_at,
            updated_at=record.updated_at,
        )"""

    def to_persistence(self):
        """return EmbeddedReportDTO(
            id=entity.id,
            title=entity.title,
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )"""

    def to_response(self):
        """return EmbeddedReportResponse(
            id=entity.id,
            title=entity.title,
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )"""
