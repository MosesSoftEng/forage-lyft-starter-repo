from abc import ABC, abstractmethod


class Battery(ABC):
    """Abstract base class representing a battery."""

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if the battery needs servicing.

        Returns:
            bool: True if the battery needs servicing, False otherwise.
        """
        pass
