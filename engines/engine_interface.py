from abc import ABC, abstractmethod


class Engine(ABC):
    """Abstract base class representing an engine."""

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if the engine needs servicing.

        Returns:
            bool: True if the engine needs servicing, False otherwise.
        """
        pass
