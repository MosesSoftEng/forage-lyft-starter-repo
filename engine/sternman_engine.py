from engine.engine_interface import Engine


class SternmanEngine(Engine):
    """
    Represents a Sternman engine that implements the Engine interface.

    Args:
        warning_light_is_on (bool): Indicates if the warning light is on.
    """

    def __init__(self, warning_light_is_on: bool):
        """
        Initialize a SternmanEngine object.

        Args:
            warning_light_is_on (bool): Indicates if the warning light is on.
        """
        self.warning_light_is_on: bool = warning_light_is_on

    def engine_should_be_serviced(self) -> bool:
        """
        Determines if the Sternman engine should be serviced.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.warning_light_is_on
