import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engines import Engines 

class Rocket:
    def __init__(self,dry_mass, fuel_mass, diameter, Cd, engine: Engines):
        self.dry_mass = dry_mass
        self.fuel_mass = fuel_mass
        self.diameter = diameter
        self.Cd = Cd
        self.engine= engine

        if not (isinstance(self.dry_mass, (int,float)) and self.dry_mass >0 and isinstance(self.fuel_mass, (int,float)) and self.fuel_mass >= 0 and isinstance(self.diameter, (int,float)) and self.diameter > 0 and isinstance(self.Cd, (int,float)) and self.Cd > 0):
             raise ValueError("Dry mass and diameter must be positive numbers. Fuel mass and Cd must be non-negative/positive numbers.")

        
    def get_mass(self):
        return self.dry_mass + self.fuel_mass 

    def get_area(self):
        return math.pi * (self.diameter/2)**2