import math
           
class Engines:
     def __init__(self, burn_time, Isp):
          self.burn_time = burn_time
          self.Isp = Isp

          if not (isinstance(self.burn_time, (int,float)) and self.burn_time >0 and isinstance(self.Isp, (int,float)) and self.Isp > 0):
               raise ValueError("Burn time and Isp must be positive numbers.")

     def get_mass_flow_rate(self, time, throttle= 1):
          return  self.get_thrust(time, throttle) / (self.Isp * 9.80665)


     def consume_fuel(self, Rocket, dt, time, throttle=1):
          fuel_to_burn = self.get_mass_flow_rate(time,throttle) * dt
          if fuel_to_burn <= Rocket.fuel_mass:
               Rocket.fuel_mass -= fuel_to_burn
               return fuel_to_burn
          else:
               fuel_consumed = Rocket.fuel_mass
               Rocket.fuel_mass = 0
               return fuel_consumed

class Solid_Engine(Engines):
     def __init__(self, burn_time, Isp, thrust_peak):
          super().__init__(burn_time, Isp)
          self.thrust_peak = thrust_peak

          if not (isinstance(self.thrust_peak, (int,float)) and self.thrust_peak > 0):
               raise ValueError("Thrust peak must be a positive number.")

     def get_thrust(self, time, throttle=1):
          if time < self.burn_time:
               return self.thrust_peak * math.sin((math.pi * time) / self.burn_time)
          else:
               return 0


class Liquid_Engine(Engines):
     def __init__(self, burn_time, Isp, thrust_max):
          super().__init__(burn_time, Isp)
          self.thrust_max = thrust_max

          if not (isinstance(self.thrust_max, (int,float)) and self.thrust_max > 0):
               raise ValueError("Maximum thrust must be a positive number.")

     def get_thrust(self, time, throttle=1):
          if time < self.burn_time:
               return self.thrust_max * throttle
          else:
               return 0
