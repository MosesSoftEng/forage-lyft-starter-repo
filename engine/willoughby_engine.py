from engine.engine_interface import Engine


class WilloughbyEngine(Engine):
    """
    Represents a Willoughby engine that implements the Engine interface.

    Args:
        current_mileage (int): The current mileage of the engine.
        last_service_mileage (int): The mileage when the engine was last
            serviced.
    """

    def __init__(self, current_mileage: int, last_service_mileage: int):
        """
        Initialize a WilloughbyEngine object.

        Args:
            current_mileage (int): The current mileage of the engine.
            last_service_mileage (int): The mileage when the engine was last
                serviced.
        """
        self.current_mileage: int = current_mileage
        self.last_service_mileage: int = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        """
        Determines if the Willoughby engine should be serviced.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage > 60000
