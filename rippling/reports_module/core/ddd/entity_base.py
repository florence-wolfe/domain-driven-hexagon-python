from abc import abstractmethod
from enum import Enum
from json import dumps
from typing import TypeVar, Generic, Protocol
from dataclasses import asdict, dataclass, field
from datetime import datetime
from uuid import UUID

AggregateID = str
EntityProps = TypeVar("EntityProps")


@dataclass
class BaseEntityProps:
    id: str
    created_at: datetime
    updated_at: datetime


def _custom_asdict_factory(data):
    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.value
        return obj

    return dict((k, convert_value(v)) for k, v in data)


@dataclass()
class Entity(Protocol, Generic[EntityProps]):
    props: EntityProps
    _id: UUID
    created_at: datetime = field(default_factory=datetime.now)
    pdated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        self.__validate_props(self.props)
        self.validate()

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)

    def to_dict(self):
        return asdict(self, dict_factory=_custom_asdict_factory)

    @abstractmethod
    def validate(self):
        """
        Validate the entity
        """
        pass

    def __validate_props(self, props: EntityProps):
        """
        Validation that applies to all entities
        """
        pass

    @classmethod
    def create(cls, create_props: EntityProps):
        ...
