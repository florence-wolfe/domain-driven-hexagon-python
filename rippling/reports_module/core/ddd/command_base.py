from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar
from uuid import UUID

from reports_module.core.guard import Guard

CommandProps = TypeVar("CommandProps")


@dataclass
class BaseCommand(Protocol, Generic[CommandProps]):
    id: UUID
    metadata: dict

    def __init__(self, props: CommandProps):
        if Guard.isEmpty(props):
            raise Exception("Props cannot be empty")
