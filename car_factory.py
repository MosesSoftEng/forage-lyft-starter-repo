from typing import List
from datetime import date

from car import Car

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    """
    A factory class for creating different types of cars.

    Methods:
        create_calliope: Create a Calliope car.
        create_glissade: Create a Glissade car.
        create_palindrome: Create a Palindrome car.
        create_rorschach: Create a Rorschach car.
        create_thovex: Create a Thovex car.
    """

    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_param: List[float]
    ) -> Car:
        """
        Create a Calliope car.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last
            `   serviced.

        Returns:
            Car: The created Calliope car.
        """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tires_param)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_param: List[float]
    ) -> Car:
        """
        Create a Glissade car.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last
                serviced.

        Returns:
            Car: The created Glissade car.
        """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tires_param)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(
        current_date: date,
        last_service_date: date,
        warning_light_is_on: bool,
        tires_param: List[float]
    ) -> Car:
        """
        Create a Palindrome car.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the car was last serviced.
            warning_light_is_on (bool): Indicates if the warning light is on.

        Returns:
            Car: The created Palindrome car.
        """
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_param)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_param: List[float]
    ) -> Car:
        """
        Create a Rorschach car.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last
            serviced.

        Returns:
            Car: The created Rorschach car.
        """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_param)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tires_param: List[float]
    ) -> Car:
        """
        Create a Thovex car.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage when the car was last
                serviced.

        Returns:
            Car: The created Thovex car.
        """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tires_param)
        return Car(engine, battery, tires)
