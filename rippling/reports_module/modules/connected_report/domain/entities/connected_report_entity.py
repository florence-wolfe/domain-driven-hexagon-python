from dataclasses import dataclass
from typing import TypedDict
from uuid import UUID

from mongoengine.fields import uuid
from reports_module.core.ddd.entity_base import Entity
from reports_module.modules.common.domain.value_objects.report_status import (
    ReportStatus,
)


class ConnectedReportProps(TypedDict):
    title: str
    status: ReportStatus


@dataclass
class ConnectedReportEntity(Entity[ConnectedReportProps]):
    _id: UUID
    props: ConnectedReportProps

    @classmethod
    def create(cls, create_props):
        id = uuid.uuid4()
        props = ConnectedReportProps(
            title=create_props["title"],
            status=ReportStatus.DRAFT,
        )
        return cls(_id=id, props=props)

    @property
    def id(self):
        return self._id

    def update_status(self, new_status):
        self.props["status"] = new_status

    def validate(self):
        pass
