from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        """
        Checks if the engine needs service based on the last service date, if the engine last serviced more than
            2 years ago engine should be serviced.

        Returns:
            bool: True if the engine needs service, False otherwise.
        """
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
