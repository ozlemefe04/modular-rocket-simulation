import math

class Environment:
       def get_air_density (self,h):
            h = max(0, h)
            air_density = 1.225 * math.exp(-h / 8500)
            return air_density
       
       def get_gravity (self, h):
            gravity = 6.67430e-11 * 5.9722e24 / (6371000 + h)**2
            return gravity

