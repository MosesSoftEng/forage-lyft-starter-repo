from engines.engine_interface import Engine


class CapuletEngine(Engine):
    """
    Represents a Capulet engine that implements the Engine interface.

    Args:
        current_mileage (int): The current mileage of the engine.
        last_service_mileage (int): The mileage when the engine was last
            serviced.
    """
    SERVICE_LIMIT_MILEAGE = 30000

    def __init__(self, current_mileage: int, last_service_mileage: int):
        """
        Initialize a CapuletEngine object.

        Args:
            current_mileage (int): The current mileage of the engine.
            last_service_mileage (int): The mileage when the engine was last
                serviced.
        """
        self.current_mileage: int = current_mileage
        self.last_service_mileage: int = last_service_mileage

    def needs_service(self) -> bool:
        """
        Determines if the Capulet engine needs servicing.

        Returns:
            bool: True if the engine needs servicing, False otherwise.
        """
        return (self.current_mileage - self.last_service_mileage >
                CapuletEngine.SERVICE_LIMIT_MILEAGE)
