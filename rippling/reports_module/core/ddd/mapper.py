from typing import Any, TypeVar, Generic, Protocol

# Define generic types for DTO and Entity
DbRecord = TypeVar("DbRecord", covariant=True)
Entity = TypeVar(
    "Entity",
)
Response = TypeVar("Response", covariant=True)


class IMapper(Protocol, Generic[Entity, DbRecord, Response]):
    def to_domain(self, record: Any) -> Entity:
        """
        Convert a DTO to a domain entity.
        Must be implemented in classes adhering to this protocol.
        """
        ...

    def to_persistence(self, entity: Entity) -> DbRecord:
        """
        Convert a domain entity to a DTO.
        Must be implemented in classes adhering to this protocol.
        """
        ...

    def to_response(self, entity: Entity) -> Response:
        """
        Convert a domain entity to a response object.
        Must be implemented in classes adhering to this protocol.
        """
        ...
