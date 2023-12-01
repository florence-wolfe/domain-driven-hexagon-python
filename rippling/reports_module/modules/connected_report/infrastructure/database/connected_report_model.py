from django_mongoengine import Document, fields
from common.document_base import DocumentBase
from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


# TODO: Add proper typing for Fields in the future by upstreaming to rippling django_mongoengine fork
class ConnectedReportModel(Document, DocumentBase):
    author = fields.StringField(verbose_name="Name", max_length=255)
    _id = fields.UUIDField(primary_key=True, binary=False)
    title = fields.StringField(max_length=200)
    content = fields.StringField()  # Using StringField for text content
    status = fields.StringField(
        max_length=50, choices=[(status, status.value) for status in ReportStatus]
    )
    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()

    # Define other fields as needed
    meta = {"collection": "connected_reports"}
