from typing import Generic, Protocol, TypeVar

Data = TypeVar("Data", contravariant=True)
Result = TypeVar("Result", covariant=True)


class BaseService(Protocol, Generic[Data, Result]):
    """
    A generic base service interface following DDD/Hexagonal Architecture principles.

    This protocol defines a single method 'execute', which should be implemented by
    any concrete service class. The method can be adapted to the specific needs of
    the domain by specifying appropriate types for its parameters and return value.

    """

    def execute(self, data: Data) -> Result:
        """
        Execute a generic action with the given input data.

        Parameters:
        data (Data): The input data for the action. The type of this parameter can be
                  any type (`Data`), depending on the specific use case.

        Returns:
        Result: The result of the action. The type of the return value can be any type (`Result`),
           depending on what the specific implementation returns.
        """
        ...
