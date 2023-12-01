from dataclasses import dataclass
from typing import Callable, Generic, Optional, Protocol, TypeVar
import asyncio

from reports_module.core.ddd.entity_base import Entity

T = TypeVar("T")
R = TypeVar("R", bound=Entity)


@dataclass
class PaginatedQueryParams:
    limit: int
    page: int
    offset: int
    orderBy: str


class BaseRepository(Protocol, Generic[R]):
    def insert(self, record: R) -> None:
        ...

    def findOneById(self, id: str) -> Optional[R]:
        ...

    def findAll(self) -> list[R]:
        ...

    def findAllPaginated(self, params: PaginatedQueryParams) -> list[R]:
        ...

    def delete(self, record: R) -> bool:
        ...

    async def transaction(
        self, handler: Callable[[], asyncio.Future[T]]
    ) -> asyncio.Future[T]:
        ...
